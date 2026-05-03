from __future__ import annotations

import argparse
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Show latest LLM Wiki rebuild progress.")
    parser.add_argument("--wiki-dir", type=Path, default=PROJECT_ROOT / "wiki")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def load_latest(wiki_dir: Path) -> dict:
    path = wiki_dir / ".staging" / "progress" / "latest-paper-run.json"
    if not path.exists():
        return {"status": "missing", "message": "No progress file exists yet."}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        return {"status": "invalid", "message": str(exc), "path": str(path)}


def load_progress_files(wiki_dir: Path) -> list[dict]:
    progress_dir = wiki_dir / ".staging" / "progress"
    if not progress_dir.exists():
        return []
    payloads = []
    for path in sorted(progress_dir.glob("paper-run-*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            continue
        payload["_path"] = str(path)
        payloads.append(payload)
    return payloads


def aggregate_shards(wiki_dir: Path, latest: dict) -> dict:
    group = latest.get("shard_group")
    if not group:
        return latest
    shards = [
        payload
        for payload in load_progress_files(wiki_dir)
        if payload.get("shard_group") == group
    ]
    if not shards:
        return latest
    shards.sort(key=lambda item: item.get("shard_index", 0))
    numeric_keys = [
        "total_records",
        "global_record_count",
        "completed",
        "skipped_complete",
        "skipped_over_budget",
        "failed",
        "remaining",
    ]
    aggregate = {
        "status": "running" if any(item.get("status") == "running" for item in shards) else shards[-1].get("status"),
        "phase": "paper-pages-sharded",
        "run_id": group,
        "shard_group": group,
        "updated_at": max((item.get("updated_at", "") for item in shards), default=""),
        "workers": len(shards),
        "shards": shards,
        "current_papers": [
            {
                "shard_index": item.get("shard_index"),
                "current_index": item.get("current_index"),
                "current_paper": item.get("current_paper"),
                "status": item.get("status"),
            }
            for item in shards
        ],
    }
    for key in numeric_keys:
        values = [item.get(key) for item in shards if isinstance(item.get(key), (int, float))]
        if values:
            if key == "global_record_count":
                aggregate[key] = max(values)
            else:
                aggregate[key] = sum(values)
    eta_values = [item.get("eta_seconds") for item in shards if isinstance(item.get("eta_seconds"), (int, float))]
    if eta_values:
        aggregate["eta_seconds"] = max(eta_values)
    eta_at_values = [item.get("eta_at") for item in shards if item.get("eta_at")]
    if eta_at_values:
        aggregate["eta_at"] = max(eta_at_values)
    avg_values = [
        item.get("avg_seconds_per_completed")
        for item in shards
        if isinstance(item.get("avg_seconds_per_completed"), (int, float))
    ]
    if avg_values:
        aggregate["avg_seconds_per_completed"] = round(sum(avg_values) / len(avg_values), 2)
    return aggregate


def main() -> int:
    args = parse_args()
    payload = aggregate_shards(args.wiki_dir, load_latest(args.wiki_dir))
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    print(f"status: {payload.get('status')}")
    print(f"phase: {payload.get('phase', '')}")
    print(f"run_id: {payload.get('run_id', '')}")
    print(f"updated_at: {payload.get('updated_at', '')}")
    for key in [
        "total_records",
        "current_index",
        "current_paper",
        "completed",
        "skipped_complete",
        "skipped_over_budget",
        "failed",
        "remaining",
        "avg_seconds_per_completed",
        "eta_seconds",
        "eta_at",
    ]:
        if key in payload:
            print(f"{key}: {payload[key]}")
    if payload.get("current_papers"):
        print("current_papers:")
        for item in payload["current_papers"]:
            print(
                f"  shard {item.get('shard_index')}: "
                f"{item.get('current_index')} {item.get('current_paper')} ({item.get('status')})"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
