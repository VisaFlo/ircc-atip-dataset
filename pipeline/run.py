"""Pipeline orchestrator: OCR markdown -> split -> classify -> dedup -> JSON.

Usage: ``python -m pipeline.run <ocr_dir> <out_dir>``

Discovers full-file OCR markdowns directly in *ocr_dir* (the ``chunks/``
subdirectory holds pre-merge page chunks and is ignored), groups them by
ATIP release number, concatenates multi-part releases in part order,
splits each release into threads, classifies quality, deduplicates
across releases, and emits the JSON dataset.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from pipeline.dedup import dedup
from pipeline.emit import emit
from pipeline.quality import classify
from pipeline.split_threads import split_threads

# ATIP release number in a filename: "A-2025-72666", "2A-2021-12699",
# "1A-2022-39382". Five digits appear in newer releases.
_RELEASE_RE = re.compile(r"((?:\d?A)-\d{4}-\d{4,5})")

# Part marker in a filename: "- Part 1", "_Part3", "_part_3".
_PART_RE = re.compile(r"part[ _-]*(\d+)", re.IGNORECASE)


def discover_releases(ocr_dir: str) -> dict[str, str]:
    """Map release number -> full OCR text (multi-part files concatenated).

    Only ``*.md`` files directly in *ocr_dir* are read (not ``chunks/``).
    Files whose names carry no release number are skipped. Parts of the
    same release are concatenated in ascending part order.
    """
    by_release: dict[str, list[tuple[int, str, Path]]] = {}
    for path in sorted(Path(ocr_dir).glob("*.md")):
        m = _RELEASE_RE.search(path.name)
        if not m:
            continue
        pm = _PART_RE.search(path.stem)
        part = int(pm.group(1)) if pm else 0
        by_release.setdefault(m.group(1), []).append((part, path.name, path))
    return {
        release: "\n\n".join(
            p.read_text(encoding="utf-8") for _, _, p in sorted(parts)
        )
        for release, parts in sorted(by_release.items())
    }


def run(ocr_dir: str, out_dir: str) -> dict:
    """Execute the full pipeline; print a summary table; return the index."""
    releases = discover_releases(ocr_dir)
    if not releases:
        print(f"no release .md files found in {ocr_dir}", file=sys.stderr)

    all_threads: list[dict] = []
    per_release: list[tuple[str, int, dict[str, int]]] = []
    for release, text in releases.items():
        threads = split_threads(text)
        counts = {"answered": 0, "deflected": 0, "partial": 0}
        for t in threads:
            t["atip_release"] = release
            t["quality"] = classify(t)
            counts[t["quality"]] += 1
        per_release.append((release, len(threads), counts))
        all_threads.extend(threads)

    before = len(all_threads)
    deduped = dedup(all_threads)
    index = emit(deduped, out_dir)

    # ---------------------------------------------------------- summary
    print(f"{'release':<16} {'threads':>7} {'answered':>8} "
          f"{'deflected':>9} {'partial':>7}")
    for release, n, c in per_release:
        print(f"{release:<16} {n:>7} {c['answered']:>8} "
              f"{c['deflected']:>9} {c['partial']:>7}")
    print(f"total threads: {before} before dedup, {index['total']} after dedup")
    print(f"by_quality after dedup: {index['by_quality']}")
    return index


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("usage: python -m pipeline.run <ocr_dir> <out_dir>",
              file=sys.stderr)
        return 2
    run(args[0], args[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
