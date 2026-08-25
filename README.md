# IRCC ATIP Dataset

<!-- STATS:HERO -->
> 32,765 pages of IRCC records obtained under the Access to Information Act,
> parsed into 7,806 searchable answers to licensed immigration representatives
> plus 32 internal officer manuals. Free, open, and still growing.
<!-- /STATS:HERO -->

<!-- STATS:BADGES -->
![source pages](https://img.shields.io/badge/source%20pages-32,765-blue)
![threads](https://img.shields.io/badge/threads-7,806-blue)
![manuals](https://img.shields.io/badge/manuals-32-blue)
![coverage](https://img.shields.io/badge/coverage-2016--2025-blue)
![data](https://img.shields.io/badge/data-OGL--Canada-green)
![code](https://img.shields.io/badge/code-MIT-green)
![updated](https://img.shields.io/badge/updated-2026--08--25-lightgrey)
<!-- /STATS:BADGES -->

**For immigration consultants, lawyers and RCICs** who need to know what IRCC has actually
said about a procedure, and **for developers and researchers** who want it as clean JSON.

Every thread traces to an ATIP package you can request yourself, free. See [`sources.md`](sources.md).

## Get the data

<!-- STATS:TABLE -->
| File | Contents | Threads |
|---|---|---|
| [`data/2016.json`](data/2016.json) | Mailbox threads, 2016 | 301 |
| [`data/2017.json`](data/2017.json) | Mailbox threads, 2017 | 555 |
| [`data/2018.json`](data/2018.json) | Mailbox threads, 2018 | 29 |
| [`data/2019.json`](data/2019.json) | Mailbox threads, 2019 | 1 |
| [`data/2020.json`](data/2020.json) | Mailbox threads, 2020 | 436 |
| [`data/2021.json`](data/2021.json) | Mailbox threads, 2021 | 2,238 |
| [`data/2022.json`](data/2022.json) | Mailbox threads, 2022 | 581 |
| [`data/2023.json`](data/2023.json) | Mailbox threads, 2023 | 2 |
| [`data/2024.json`](data/2024.json) | Mailbox threads, 2024 | 1,629 |
| [`data/2025.json`](data/2025.json) | Mailbox threads, 2025 | 1,669 |
| [`data/undated.json`](data/undated.json) | Threads with no parseable date | 365 |
| [`data/index.json`](data/index.json) | Counts by year, quality, ATIP release | — |
| [`manuals/`](manuals/) | OCR text of 32 internal IRCC documents | — |
| [Releases](../../releases) | Raw ATIP PDFs, as IRCC delivered them | — |
<!-- /STATS:TABLE -->

**Working with it in code?** No clone, no dependencies:

```python
import json, urllib.request

BASE = "https://raw.githubusercontent.com/VisaFlo/ircc-atip-dataset/main/data"
index = json.load(urllib.request.urlopen(f"{BASE}/index.json"))

threads = []
for year in index["by_year"]:
    threads += json.load(urllib.request.urlopen(f"{BASE}/{year}.json"))["threads"]

hits = [t for t in threads if "biometric" in (t.get("answer") or "").lower()]
print(len(threads), "threads,", len(hits), "mentioning biometrics")
```

## How to use it (no coding)

**Just want to look something up?** Open a year file on GitHub and use your browser's
find (Cmd/Ctrl+F). `data/2025.json` is the most recent year; each entry has the
representative's question and IRCC's reply in full.

**Prefer a spreadsheet?** Every file is JSON. Paste one into any free JSON-to-CSV
converter and open it in Excel or Google Sheets, then filter by `subject` or `quality`.

**Want the original document?** Every entry lists its `atip_release` (for example
`A-2025-72666`). The matching PDF, exactly as IRCC released it, is under
[Releases](../../releases). That's what you'd cite or show a client.

**What's actually in here.** Some counts, so you know whether it's worth your time:

| Topic | Threads mentioning it |
|---|---|
| Study permits | 927 |
| PGWP | 428 |
| Spousal / common-law | 212 |
| Police certificates | 41 |
| Proof of funds | 24 |

A caution worth repeating: these are IRCC's procedural answers to other representatives,
at the time they were written. Policy moves. Treat a thread as a lead to verify, not as
current authority, and check the date on every one.

## Ask it in plain language (VisaFlo MCP)

Searching JSON is fine for developers. Most practitioners would rather just ask.

We're wiring this dataset into VisaFlo's MCP server, so an AI assistant can search it for
you and answer with the actual IRCC reply, quoted and dated:

> *"What has IRCC said about study permits becoming invalid after completing a program?"*
>
> *"Has IRCC answered anything about remote-officiant marriages for sponsorship?"*

You get the matching threads, then the full text of the one you care about, with its ATIP
release number so you can check the original PDF yourself.

**Want access?** Email **info@vflo.app** and we'll set you up. It's rolling out to VisaFlo
accounts first; tell us what you'd search for and we'll prioritise accordingly.

The dataset stays free and open either way. The MCP is a convenience layer on top of the
same files in this repo, and it always will be.

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

## A record

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

**Fields** — `id` · `atip_release` · `date` · `subject` · `question` · `answer` · `quality`.
Full types and semantics in [`schema.md`](schema.md).

<!-- STATS:QUALITY -->
`quality` is the field to read first: `answered` (5,935) substantive reply ·
`deflected` (152) boilerplate refusal or redirect · `partial` (1,719) OCR-torn or empty.
<!-- /STATS:QUALITY -->

Deflected threads are kept, not hidden. What IRCC declines to answer is signal too.

## What else is inside

- **`manuals/`** — OCR text of 19 internal IRCC documents: the Chinook processing manuals
  (including the refusal-notes generator), R10 completeness manuals, ENF 2 inadmissibility
  assessment, the Express Entry officer answer guide, anti-fraud manual, Country Information
  Library. Each file carries its provenance.
- **`pipeline/`** — the parsing pipeline (OCR text → threads → dedup → JSON), stdlib-only
  Python, 90+ tests. Clone and run it on your own ATIP packages.
- **[`sources.md`](sources.md)** — every ATIP request number, and the steps to obtain the
  same records free.

## Limitations

- Source documents are scanned PDFs; text is local-OCR output and carries OCR noise.
- `question`/`answer` extraction is best-effort; `quality: partial` marks OCR-torn threads
  rather than hiding them.
- IRCC's replies are procedural guidance at the time of writing, not legal advice.
  Always verify against current IRCC instructions.

Found a mis-parsed thread, a wrong date, or personal information that should have been
redacted? [Open an issue](../../issues/new) with the thread `id`. We fix data bugs the
same way we fix code bugs.

## How to help

- **Know a completed IRCC ATIP request that belongs here?** Open an issue with the request
  number. We re-request it and add it.
- Spot a parsing error, improve the pipeline, or add a category taxonomy: PRs welcome.

## Roadmap

See [ROADMAP.md](ROADMAP.md) — GCMS codes reference, response-template corpus, Functional
Guidance repository, and more packages currently ingesting.

## Citation

```bibtex
@misc{irccatip2026,
  title  = {IRCC ATIP Dataset: Records Released under the Access to Information Act},
  author = {{VisaFlo}},
  year   = {2026},
  url    = {https://github.com/VisaFlo/ircc-atip-dataset},
  note   = {Records released under the Access to Information Act (Canada)}
}
```

## About

We're [VisaFlo](https://vflo.app). We build case management for Canadian immigration
practices, working toward a simple idea: **a better migrating world**, where every case
knows what comes next and safely gets there.

We also make this searchable inside our product. The data here is the same data, and
always will be.

This dataset is our contribution to the people doing that work. The records were always
public. Now they're usable.

Data: released under the Access to Information Act; contains information licensed under the
Open Government Licence – Canada. Code: MIT.
Removal requests / questions: open an issue or info@vflo.app.
