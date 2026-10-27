#!/usr/bin/env python3
"""Render border_context_pack.md from border_context_pack.json.

This keeps the human-readable research note reproducible after curated JSON edits.
Run from any directory; output overwrites the Markdown file only when explicitly run.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "border_context_pack.json"
MD_PATH = ROOT / "border_context_pack.md"


def corruption_text(value: Any) -> str:
    if value is None:
        return "Not applicable/reliably comparable for this entry in this pack."
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        score = value.get("score")
        year = value.get("year")
        source = value.get("source")
        if score is None:
            return "Not applicable/reliably comparable for this entry in this pack."
        if source and year:
            return f"{score}/100, {source} ({year})."
        if source:
            return f"{score}/100, {source}."
        return f"{score}/100."
    return str(value)


def render_entry(entry: dict[str, Any]) -> list[str]:
    lines = [
        f"## {entry['name']} (`{entry['id']}`)",
        "",
        f"**Type:** {entry['type']}",
        "",
        "**Border history**",
    ]
    lines.extend(f"- {item}" for item in entry["border_history"])
    lines.extend([
        "",
        f"**Human-cost tags:** {', '.join(entry['human_cost_tags'])}",
        "",
        f"**Government context:** {entry['government_context']}",
        "",
        f"**Languages:** {entry['languages']}",
        "",
        f"**Corruption context:** {corruption_text(entry['corruption_context'])}",
        "",
        "**Sources**",
    ])
    lines.extend(f"- {source}" for source in entry["sources"])
    lines.append("")
    return lines


def render(data: dict[str, Any]) -> str:
    lines = [
        "# MapTight border context pack",
        "",
        f"Version: {data['version']}",
        "",
        "Curated short-form context for UI import. Keep copy neutral: borders are historical/political artifacts, not destiny.",
        "",
        "## Implementation notes",
        "",
    ]
    for note in data.get("notes", []):
        lines.append(f"- {note}")
    lines.extend([
        "",
        "- Load `border_context_pack.json` as external data later instead of embedding in `index.html`.",
        "- Match entries by stable `id` values already used in app data/presets where possible.",
        "- In UI, show 3–5 `border_history` bullets plus tags; keep sources collapsed behind a “sources” link.",
        "- `corruption_context` is null for regions, U.S. states, and entities without reliable CPI coverage.",
        "- Treat this as v1: source-check before adding casualty numbers, contested-boundary claims, or sensitive map labels.",
        "",
    ])
    for entry in data["entries"]:
        lines.extend(render_entry(entry))
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if Markdown is not in sync; do not write")
    args = parser.parse_args()

    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    rendered = render(data)
    if args.check:
        current = MD_PATH.read_text(encoding="utf-8")
        if current != rendered:
            raise SystemExit(f"{MD_PATH.relative_to(ROOT.parent)} is out of sync; run this script without --check")
        print(f"OK: {MD_PATH.relative_to(ROOT.parent)} is in sync with {len(data['entries'])} entries")
        return

    MD_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote {MD_PATH.relative_to(ROOT.parent)} with {len(data['entries'])} entries")


if __name__ == "__main__":
    main()
