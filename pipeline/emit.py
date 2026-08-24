"""Emit parsed threads as the public JSON dataset.

``emit(threads, out_dir)`` writes one ``<year>.json`` per calendar year
(plus ``undated.json``) and an ``index.json`` summary into *out_dir*, and
returns the index dict. Output records carry only the public fields —
``raw`` (the huge OCR text) is deliberately dropped; the JSON is the
product. Stdlib only.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import date as _date

from pipeline.quality import classify

# The public record schema, in emission order.
RECORD_KEYS = (
    "id", "atip_release", "date", "subject", "question", "answer",
    "quality", "category", "tags",
)

# Registry stamps seen in subjects/raw: "REP-2025-0939", and the lettered
# variant "REP-B-2025-1767".
_REP_ID_RE = re.compile(r"REP-(?:[A-Z]-)?\d{4}-\d{4}")


def make_id(thread: dict) -> str:
    """Canonical id for a thread: its REP registry stamp, else a content hash.

    The REP number is looked for in the subject first, then in the raw OCR
    text. Without one, the id is ``GEN-`` + first 8 hex chars of
    sha256(subject + date + first 200 chars of raw) — deterministic across
    runs for the same input.
    """
    for source in (thread.get("subject"), thread.get("raw")):
        if source:
            m = _REP_ID_RE.search(source)
            if m:
                return m.group(0)
    material = (
        (thread.get("subject") or "")
        + (thread.get("date") or "")
        + (thread.get("raw") or "")[:200]
    )
    return "GEN-" + hashlib.sha256(material.encode("utf-8")).hexdigest()[:8]


def _releases(thread: dict) -> list[str]:
    r = thread.get("atip_release")
    if r is None:
        return []
    if isinstance(r, list):
        return sorted(r)
    return [r]


def _to_record(thread: dict, thread_id: str) -> dict:
    quality = thread.get("quality") or classify(thread)
    return {
        "id": thread_id,
        "atip_release": _releases(thread),
        "date": thread.get("date"),
        "subject": thread.get("subject") or "",
        "question": thread.get("question"),
        "answer": thread.get("answer"),
        "quality": quality,
        "category": None,
        "tags": [],
    }


def emit(threads: list[dict], out_dir: str) -> dict:
    """Write year-grouped JSON files + index.json; return the index dict."""
    os.makedirs(out_dir, exist_ok=True)

    # Assign collision-safe ids in input order (suffix -2, -3, ... on repeat).
    used: dict[str, int] = {}
    records: list[dict] = []
    for thread in threads:
        base = make_id(thread)
        n = used.get(base, 0) + 1
        used[base] = n
        records.append(_to_record(thread, base if n == 1 else f"{base}-{n}"))

    # Group by year of date; dateless records go to "undated".
    groups: dict[str, list[dict]] = {}
    for rec in records:
        key = rec["date"][:4] if rec["date"] else "undated"
        groups.setdefault(key, []).append(rec)

    for key, recs in groups.items():
        recs.sort(key=lambda r: (r["date"] or "", r["id"]))
        path = os.path.join(out_dir, f"{key}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"threads": recs, "count": len(recs)}, fh,
                      ensure_ascii=False, indent=1)
            fh.write("\n")

    by_quality: dict[str, int] = {}
    by_release: dict[str, int] = {}
    for rec in records:
        by_quality[rec["quality"]] = by_quality.get(rec["quality"], 0) + 1
        for rel in rec["atip_release"]:
            by_release[rel] = by_release.get(rel, 0) + 1

    index = {
        "total": len(records),
        "by_year": {k: len(v) for k, v in sorted(groups.items())},
        "by_quality": dict(sorted(by_quality.items())),
        "by_release": dict(sorted(by_release.items())),
        "generated": _date.today().isoformat(),
    }
    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    return index
