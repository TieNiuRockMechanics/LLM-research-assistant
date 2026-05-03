import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path


DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
SCIENCEDIRECT_PII_RE = re.compile(r"/pii/([^?#/]+)", re.I)


def clean_doi(value: str) -> str:
    if not value:
        return ""
    value = urllib.parse.unquote(str(value)).strip()
    value = value.replace("https://doi.org/", "").replace("http://doi.org/", "")
    match = DOI_RE.search(value)
    if not match:
        return ""
    doi = match.group(0).rstrip(".,);]").lower()
    return doi


def clean_title(title: str) -> str:
    title = (title or "").strip()
    replacements = [
        r"\s*-\s*ScienceDirect\s*$",
        r"\s*-\s*ScienceDirect\.com\s*$",
        r"\s*-\s*All Databases\s*\([^)]*\)\s*$",
        r"\s*\|\s*.*(?:springer|wiley|frontiers|mdpi|hindawi|clarivate|cnki)\.?(?:com|cn)?\)?\s*$",
        r"\s*\([^)]*(?:springer|wiley|frontiers|mdpi|hindawi|clarivate|cnki|sciencedirect)[^)]*\)\s*$",
    ]
    for pattern in replacements:
        title = re.sub(pattern, "", title, flags=re.I)
    title = re.sub(r"\s+", " ", title).strip(" -|")
    return title


def normalize_text(value: str) -> str:
    value = (value or "").lower()
    value = re.sub(r"&", " and ", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def title_similarity(left: str, right: str) -> float:
    left_norm = normalize_text(left)
    right_norm = normalize_text(right)
    if not left_norm or not right_norm:
        return 0.0
    if left_norm == right_norm:
        return 1.0
    return SequenceMatcher(None, left_norm, right_norm).ratio()


def request_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "zotero-paperqa-assistant DOI lookup (local research library; mailto:unknown@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def crossref_lookup(title: str, rows: int = 5) -> list[dict]:
    query = urllib.parse.urlencode(
        {
            "query.title": title,
            "rows": str(rows),
            "select": "DOI,title,container-title,issued,URL,score,type",
        }
    )
    url = f"https://api.crossref.org/works?{query}"
    data = request_json(url)
    items = data.get("message", {}).get("items", [])
    results = []
    for item in items:
        titles = item.get("title") or []
        candidate_title = titles[0] if titles else ""
        doi = clean_doi(item.get("DOI", ""))
        if not doi or not candidate_title:
            continue
        results.append(
            {
                "provider": "crossref",
                "doi": doi,
                "candidate_title": candidate_title,
                "similarity": title_similarity(title, candidate_title),
                "score": item.get("score", ""),
                "url": item.get("URL", ""),
                "raw": item,
            }
        )
    return results


def openalex_lookup(title: str, rows: int = 5) -> list[dict]:
    query = urllib.parse.urlencode(
        {
            "search": title,
            "per-page": str(rows),
            "select": "id,doi,title,display_name,publication_year",
        }
    )
    url = f"https://api.openalex.org/works?{query}"
    data = request_json(url)
    items = data.get("results", [])
    results = []
    for item in items:
        candidate_title = item.get("title") or item.get("display_name") or ""
        doi = clean_doi(item.get("doi", ""))
        if not doi or not candidate_title:
            continue
        results.append(
            {
                "provider": "openalex",
                "doi": doi,
                "candidate_title": candidate_title,
                "similarity": title_similarity(title, candidate_title),
                "score": "",
                "url": item.get("id", ""),
                "raw": item,
            }
        )
    return results


def extract_sciencedirect_pii(url: str) -> str:
    match = SCIENCEDIRECT_PII_RE.search(url or "")
    return match.group(1) if match else ""


def publisher_meta_doi_lookup(url: str) -> list[dict]:
    if not url:
        return []
    host = urllib.parse.urlparse(url).netloc.lower()
    if host not in {"www.mdpi.com", "mdpi.com"}:
        return []
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "zotero-paperqa-assistant DOI lookup (local research library; mailto:unknown@example.com)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", "ignore")
    match = re.search(r'<meta[^>]+name=["\']citation_doi["\'][^>]+content=["\']([^"\']+)', html, re.I)
    if not match:
        match = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_doi["\']', html, re.I)
    doi = clean_doi(match.group(1) if match else "")
    if not doi:
        return []
    return [
        {
            "provider": "publisher_meta",
            "doi": doi,
            "candidate_title": "",
            "similarity": 1.0,
            "score": "",
            "url": url,
            "raw": {},
        }
    ]


def crossref_pii_lookup(pii: str, rows: int = 3) -> list[dict]:
    if not pii:
        return []
    query = urllib.parse.urlencode(
        {
            "query": pii,
            "rows": str(rows),
            "select": "DOI,title,container-title,issued,URL,score,type",
        }
    )
    url = f"https://api.crossref.org/works?{query}"
    data = request_json(url)
    items = data.get("message", {}).get("items", [])
    results = []
    for item in items:
        titles = item.get("title") or []
        candidate_title = titles[0] if titles else ""
        doi = clean_doi(item.get("DOI", ""))
        score = float(item.get("score") or 0.0)
        if not doi or not candidate_title or score < 7.0:
            continue
        results.append(
            {
                "provider": "crossref_pii",
                "doi": doi,
                "candidate_title": candidate_title,
                "similarity": min(1.0, score / 12.0),
                "score": score,
                "url": item.get("URL", ""),
                "raw": item,
            }
        )
    return results


def classify_candidate(candidate: dict) -> tuple[str, str]:
    if candidate.get("provider") == "publisher_meta":
        return "found", "high"
    if candidate.get("provider") == "crossref_pii":
        score = float(candidate.get("score") or 0.0)
        if score >= 10.0:
            return "found", "high"
        if score >= 7.0:
            return "found", "medium"
    similarity = float(candidate.get("similarity") or 0.0)
    if similarity >= 0.92:
        return "found", "high"
    if similarity >= 0.84:
        return "found", "medium"
    if similarity >= 0.74:
        return "review", "low"
    return "unresolved", "none"


def best_lookup(title: str, url: str, sleep_seconds: float) -> tuple[str, str, str, list[dict]]:
    candidates = []
    try:
        candidates.extend(publisher_meta_doi_lookup(url))
    except Exception as exc:  # noqa: BLE001 - record API failures without stopping the batch.
        candidates.append(
            {
                "provider": "publisher_meta",
                "doi": "",
                "candidate_title": "",
                "similarity": 0.0,
                "score": "",
                "url": "",
                "error": str(exc),
            }
        )
    if any(item.get("doi") and item.get("provider") == "publisher_meta" for item in candidates):
        best = next(item for item in candidates if item.get("doi") and item.get("provider") == "publisher_meta")
        return best["doi"], best["provider"], "high", candidates

    pii = extract_sciencedirect_pii(url)
    if pii:
        try:
            candidates.extend(crossref_pii_lookup(pii))
        except Exception as exc:  # noqa: BLE001 - record API failures without stopping the batch.
            candidates.append(
                {
                    "provider": "crossref_pii",
                    "doi": "",
                    "candidate_title": "",
                    "similarity": 0.0,
                    "score": "",
                    "url": "",
                    "error": str(exc),
                }
            )
        time.sleep(sleep_seconds)

    for lookup in (crossref_lookup, openalex_lookup):
        try:
            candidates.extend(lookup(title))
        except Exception as exc:  # noqa: BLE001 - record API failures without stopping the batch.
            candidates.append(
                {
                    "provider": lookup.__name__.replace("_lookup", ""),
                    "doi": "",
                    "candidate_title": "",
                    "similarity": 0.0,
                    "score": "",
                    "url": "",
                    "error": str(exc),
                }
            )
        time.sleep(sleep_seconds)

    valid = [item for item in candidates if item.get("doi")]
    valid.sort(key=lambda item: float(item.get("similarity") or 0.0), reverse=True)
    if not valid:
        return "", "unresolved", "none", candidates

    best = valid[0]
    status, confidence = classify_candidate(best)
    if status == "found":
        return best["doi"], best["provider"], confidence, candidates
    return "", status, confidence, candidates


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/temp-excel-doi/doi_manifest.csv")
    parser.add_argument("--output-dir", default="data/temp-excel-doi")
    parser.add_argument("--sleep", type=float, default=0.25)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))

    lookup_rows = []
    enriched_rows = []
    all_dois_in_row_order = []
    unresolved_rows = []

    for row in rows:
        source_doi = clean_doi(row.get("doi", ""))
        url_doi = clean_doi(row.get("url", ""))
        title_doi = clean_doi(row.get("title", ""))
        existing_doi = source_doi or url_doi or title_doi
        cleaned_title = clean_title(row.get("title", ""))

        doi = existing_doi
        lookup_source = row.get("doi_source") or ("url_or_title" if (url_doi or title_doi) else "")
        confidence = "exact" if existing_doi else ""
        status = "existing" if existing_doi else "pending"
        candidates = []

        if not existing_doi:
            doi, lookup_source, confidence, candidates = best_lookup(cleaned_title, row.get("url", ""), args.sleep)
            status = "found" if doi else lookup_source

        if doi:
            all_dois_in_row_order.append(doi)
        else:
            unresolved_rows.append(
                {
                    "row": row.get("row", ""),
                    "title": row.get("title", ""),
                    "cleaned_title": cleaned_title,
                    "url": row.get("url", ""),
                    "domain": row.get("domain", ""),
                    "lookup_status": status,
                    "confidence": confidence,
                }
            )

        best_candidate = ""
        best_candidate_title = ""
        best_similarity = ""
        best_provider = ""
        best_url = ""
        candidate_errors = []
        valid_candidates = [item for item in candidates if item.get("doi")]
        valid_candidates.sort(key=lambda item: float(item.get("similarity") or 0.0), reverse=True)
        if valid_candidates:
            best = valid_candidates[0]
            best_candidate = best.get("doi", "")
            best_candidate_title = best.get("candidate_title", "")
            best_similarity = f"{float(best.get('similarity') or 0.0):.3f}"
            best_provider = best.get("provider", "")
            best_url = best.get("url", "")
        for item in candidates:
            if item.get("error"):
                candidate_errors.append(f"{item.get('provider')}: {item.get('error')}")

        enriched = dict(row)
        enriched.update(
            {
                "cleaned_title": cleaned_title,
                "doi_enriched": doi,
                "doi_enriched_source": lookup_source,
                "doi_confidence": confidence,
                "lookup_status": status,
            }
        )
        enriched_rows.append(enriched)

        if not existing_doi:
            lookup_rows.append(
                {
                    "row": row.get("row", ""),
                    "title": row.get("title", ""),
                    "cleaned_title": cleaned_title,
                    "url": row.get("url", ""),
                    "domain": row.get("domain", ""),
                    "doi_enriched": doi,
                    "lookup_status": status,
                    "doi_confidence": confidence,
                    "best_candidate_doi": best_candidate,
                    "best_candidate_provider": best_provider,
                    "best_candidate_similarity": best_similarity,
                    "best_candidate_title": best_candidate_title,
                    "best_candidate_url": best_url,
                    "errors": " | ".join(candidate_errors),
                }
            )

    unique_dois = []
    seen = set()
    for doi in all_dois_in_row_order:
        if doi not in seen:
            seen.add(doi)
            unique_dois.append(doi)

    enriched_fields = list(enriched_rows[0].keys()) if enriched_rows else []
    write_csv(output_dir / "doi_manifest_enriched.csv", enriched_rows, enriched_fields)
    write_csv(
        output_dir / "doi_external_lookup_results.csv",
        lookup_rows,
        [
            "row",
            "title",
            "cleaned_title",
            "url",
            "domain",
            "doi_enriched",
            "lookup_status",
            "doi_confidence",
            "best_candidate_doi",
            "best_candidate_provider",
            "best_candidate_similarity",
            "best_candidate_title",
            "best_candidate_url",
            "errors",
        ],
    )
    write_csv(
        output_dir / "doi_unresolved_after_lookup.csv",
        unresolved_rows,
        ["row", "title", "cleaned_title", "url", "domain", "lookup_status", "confidence"],
    )

    (output_dir / "doi_list_all_unique.txt").write_text("\n".join(unique_dois) + "\n", encoding="utf-8")
    (output_dir / "doi_list_all_by_excel_row.txt").write_text(
        "\n".join(all_dois_in_row_order) + "\n", encoding="utf-8"
    )

    summary = {
        "input": str(input_path.resolve()),
        "records": len(rows),
        "original_with_doi": sum(1 for row in rows if clean_doi(row.get("doi", ""))),
        "found_by_external_lookup": sum(1 for row in lookup_rows if row["doi_enriched"]),
        "lookup_review_only": sum(1 for row in lookup_rows if row["lookup_status"] == "review"),
        "unresolved": len(unresolved_rows),
        "all_records_with_doi_after_lookup": len(all_dois_in_row_order),
        "unique_dois_after_lookup": len(unique_dois),
        "outputs": {
            "enriched_manifest": str((output_dir / "doi_manifest_enriched.csv").resolve()),
            "external_lookup_results": str((output_dir / "doi_external_lookup_results.csv").resolve()),
            "unresolved": str((output_dir / "doi_unresolved_after_lookup.csv").resolve()),
            "unique_doi_list": str((output_dir / "doi_list_all_unique.txt").resolve()),
            "row_order_doi_list": str((output_dir / "doi_list_all_by_excel_row.txt").resolve()),
        },
    }
    (output_dir / "external_lookup_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
