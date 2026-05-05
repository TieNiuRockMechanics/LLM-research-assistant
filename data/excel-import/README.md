# Excel Paper Import

Generated from:

```text
C:\Users\shuixin2\Desktop\论文参考文献.xlsx
```

Recommended workflow:

1. Review `summary.json` and `excel_papers_manifest.csv`.
2. In Zotero, import high-quality metadata first:
   - Use `doi_list.txt` with Zotero's Add Item by Identifier for DOI-backed records.
   - Use `zotero_non_doi_placeholders.ris` for records without DOI.
   - Do not import both `doi_list.txt` and `zotero_all_records_with_excel_notes.ris` into the same Zotero library unless you plan to merge duplicates.
   - `zotero_all_records_with_excel_notes.ris` is kept as a complete fallback/archive with Excel notes.
3. Use Zotero Connector / Find Available PDFs to attach PDFs.
4. Use `manual_access_required.csv` for records likely needing institution login, VPN, CNKI, ScienceDirect, Wiley, or ACS access.
5. Use `auto_pdf_candidates.csv` for records likely suitable for automatic public PDF checks.
6. Review `book_or_longform_candidates.csv`; these should not enter the normal paper indexing path.

Do not directly edit Zotero's SQLite database. Let Zotero import and manage items.
