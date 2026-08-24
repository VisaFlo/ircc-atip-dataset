# Open IRCC Dataset

**Public records about Canadian immigration, made actually usable.
Structured Q&A from IRCC's Immigration Representatives Mailbox, internal officer manuals,
and the raw ATIP releases behind them. Free, open, verifiable, growing daily.**

## Why this exists

Immigration runs on information, and too much of it is locked up.

The answers IRCC gives to licensed representatives sit in Access to Information queues.
The manuals officers actually use to assess applications never make it to the public
instructions. What does get released comes out as thousands of pages of scanned,
unsearchable PDF, scattered across request numbers nobody can find. Some of it ends up
behind paywalls.

People make life decisions on this information. Representatives argue cases on it.
It should not take a FOIA workflow and OCR pipeline to read it.

So we built the pipeline once, and opened everything.

## What's inside

- **`data/`** — IRCC's answers to representatives (Immigration Representatives Mailbox),
  parsed into thread-level JSON: subject, the rep's question, IRCC's answer, date, quality
  flag, source ATIP package. 924 threads live, thousands more landing as packages arrive.
  See [`schema.md`](schema.md).
- **`manuals/`** — OCR text of 18 internal IRCC documents: the Chinook processing manuals
  (including the refusal-notes generator module), R10 completeness manuals, ENF 2
  inadmissibility assessment, the Express Entry officer answer guide, anti-fraud manual,
  Country Information Library, and more. Each file carries its provenance.
- **Releases** — the raw ATIP release PDFs exactly as IRCC delivered them (IRCC's own
  s.19(1) redactions), so every parsed line can be checked against its source.
- **`pipeline/`** — the full parsing pipeline (OCR text → threads → dedup → JSON),
  stdlib-only Python, 90+ tests. Clone and run it on your own ATIP packages.
- **[`sources.md`](sources.md)** — every ATIP request number, and how anyone can obtain
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
- `question`/`answer` extraction is best-effort; `quality: partial` marks OCR-torn threads
  rather than hiding them.
- IRCC's replies are procedural guidance at the time of writing, not legal advice.
  Always verify against current IRCC instructions.

## Roadmap
See [ROADMAP.md](ROADMAP.md) — GCMS codes reference, response-template corpus, police
certificate country matrix, program checklists, and search inside
[VisaFlo](https://vflo.app) are all on deck.

## About

We're [VisaFlo](https://vflo.app). We build case management for Canadian immigration
practices, working toward a simple idea: **a better migrating world**, where every case
knows what comes next and safely gets there.

This dataset is our contribution to the people doing that work. The records were always
public. Now they're usable.

Data: released under the Access to Information Act; contains information licensed under the
Open Government Licence – Canada. Code: MIT.
Removal requests / questions: open an issue or support@vflo.app.
