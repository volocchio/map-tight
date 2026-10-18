#!/usr/bin/env python3
"""Lightweight validator for MapTight border_context_pack files.

Checks JSON syntax/basic shape, duplicate IDs, source lists, and whether every JSON
entry has a matching Markdown section of the form: ## Name (`id`).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "border_context_pack.json"
MD_PATH = ROOT / "border_context_pack.md"
REQUIRED_ENTRY_KEYS = {
    "id",
    "name",
    "type",
    "border_history",
    "human_cost_tags",
    "government_context",
    "languages",
    "corruption_context",
    "sources",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("top-level JSON must be an object")
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        fail("entries must be a non-empty list")

    seen: set[str] = set()
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            fail(f"entry {index} is not an object")
        missing = REQUIRED_ENTRY_KEYS - set(entry)
        if missing:
            fail(f"entry {index} missing keys: {sorted(missing)}")
        entry_id = entry["id"]
        if not isinstance(entry_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry_id):
            fail(f"entry {index} has invalid id: {entry_id!r}")
        if entry_id in seen:
            fail(f"duplicate id: {entry_id}")
        seen.add(entry_id)
        if not isinstance(entry["border_history"], list) or len(entry["border_history"]) < 3:
            fail(f"{entry_id}: border_history should have at least 3 bullets")
        if not isinstance(entry["human_cost_tags"], list) or not entry["human_cost_tags"]:
            fail(f"{entry_id}: human_cost_tags must be a non-empty list")
        if not isinstance(entry["sources"], list) or not entry["sources"]:
            fail(f"{entry_id}: sources must be a non-empty list")
        for source in entry["sources"]:
            if not isinstance(source, str) or not source.startswith(("https://", "http://")):
                fail(f"{entry_id}: suspicious source URL: {source!r}")

    md = MD_PATH.read_text(encoding="utf-8")
    md_ids = set(re.findall(r"^## .+? \(`([^`]+)`\)\s*$", md, flags=re.MULTILINE))
    missing_md = sorted(seen - md_ids)
    extra_md = sorted(md_ids - seen)
    if missing_md:
        fail(f"JSON ids missing from Markdown: {missing_md}")
    if extra_md:
        fail(f"Markdown ids missing from JSON: {extra_md}")

    print(f"OK: {len(entries)} entries validated; JSON and Markdown ids match")


if __name__ == "__main__":
    main()
