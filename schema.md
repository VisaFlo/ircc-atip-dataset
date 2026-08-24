# Thread Schema

Each record in `data/*.json`:

| field | type | description |
|---|---|---|
| `id` | string | IRCC's own tracking id when present (`REP-2025-0939`, `REP-B-2025-1767`), else deterministic `GEN-<sha256-8>` |
| `atip_release` | string[] | ATIP request number(s) this thread was released under — see `sources.md` |
| `date` | string \| null | ISO date of IRCC's reply email (best-effort OCR parse) |
| `subject` | string | Email subject, RE:/FW: prefixes stripped |
| `question` | string \| null | The representative's question (best-effort extraction) |
| `answer` | string \| null | IRCC's reply body (best-effort extraction) |
| `quality` | string | `answered` — substantive reply · `deflected` — boilerplate refusal/redirect only · `partial` — OCR-torn or empty |
| `category` | null | reserved (coming) |
| `tags` | [] | reserved (coming) |

Notes:
- Source documents are scanned PDFs released under the Access to Information Act; text passed through local OCR. Expect OCR noise — `raw` page images remain authoritative and every thread is traceable to its release package via `atip_release`.
- `deflected` threads are kept, not hidden: what IRCC declines to answer is signal too.
