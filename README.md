# IRCC Immigration Representatives Mailbox — Open Dataset

**924 real IRCC answers to Canadian immigration representatives — structured, searchable, free.
Growing daily as more ATIP packages land (13 more ingesting, ~30,000 pages total).**

IRCC runs a dedicated mailbox where licensed representatives (RCICs, immigration lawyers)
ask procedural questions and get official answers. Those answers shape real cases every day —
but they were only accessible through Access to Information requests, or behind paywalls.

This repo makes them free and open:

- `data/*.json` — one file per year, thread-level records: subject, question, IRCC's answer,
  date, quality flag, source ATIP package. See [`schema.md`](schema.md).
- `pipeline/` — the full parsing pipeline (OCR text → threads → dedup → JSON), stdlib-only
  Python, 90+ tests. Clone and run it on your own ATIP packages.
- [`sources.md`](sources.md) — every source ATIP request number, and how anyone can obtain
  the same records free to verify this dataset.

## Quick look

```json
{
  "id": "REP-2017-0386",
  "atip_release": ["A-2021-10864"],
  "date": "2017-03-08",
  "subject": "URGENT-Portal Issues-IMM 5710-REP-2017-0386-",
  "question": "…issue with the current IMM 5710 form (12-2016 version)…",
  "answer": "There is a known problem with the IMM5710 version 12/2016. We are working to address this…",
  "quality": "answered"
}
```

## Honest limitations
- Source documents are scanned PDFs; text is local-OCR output and carries OCR noise.
- `question`/`answer` extraction is best-effort (email chains are messy); `quality: partial`
  marks OCR-torn threads rather than hiding them.
- IRCC's replies are procedural guidance, not legal advice, and reflect policy at the time
  of writing. Always verify against current IRCC instructions.

## Roadmap
- 13 more ATIP packages ingesting (2016–2025 full coverage, ~5,000+ threads expected)
- Category/tag enrichment
- Search via VisaFlo's MCP server — ask your AI assistant "what did IRCC say about X?"

---
Maintained by [VisaFlo](https://vflo.app) — case management built for Canadian immigration
practices. This dataset is our contribution to the practitioner community: the answers were
always public records; now they're usable.

Data: released under the Access to Information Act, contains information licensed under the
Open Government Licence – Canada. Code: MIT.
