#!/usr/bin/env python3
"""Audit Fundamentals Markdown relative paths and GitHub-style heading fragments.

Scope: simple inline Markdown links/images, reference definitions, and HTML href/src.
Does not fetch external URLs or claim full CommonMark parsing or source verification.
Run: python3 foundations/fundamentals/tools/check_internal_links.py
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[3]
CORPUS = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
LINK = re.compile(r"!?(?:\[[^\]]*\])\(\s*(<[^>]+>|[^\s)]+)")
REF = re.compile(r"^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)")
HTML_LINK = re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.I)
NAMED_ANCHOR = re.compile(r"\b(?:id|name)\s*=\s*[\"']([^\"']+)[\"']", re.I)


def active_lines(source: str):
    fence_char = None
    fence_len = 0
    for number, line in enumerate(source.splitlines(), 1):
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char, fence_len = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len:
                fence_char, fence_len = None, 0
            continue
        if fence_char is None:
            yield number, line


def github_slug(title: str) -> str:
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"!?(?:\[([^\]]*)\])\([^)]*\)", r"\1", title)
    title = title.replace("`", "").replace("*", "").replace("~", "")
    title = html.unescape(title).lower().strip()
    return re.sub(r"[^\w\- ]", "", title).replace(" ", "-")


anchor_cache: dict[Path, set[str]] = {}


def anchors(path: Path) -> set[str]:
    if path in anchor_cache:
        return anchor_cache[path]
    seen: dict[str, int] = {}
    found: set[str] = set()
    for _, line in active_lines(path.read_text(encoding="utf-8")):
        match = HEADING.match(line)
        if match:
            base = github_slug(match.group(1))
            count = seen.get(base, 0)
            seen[base] = count + 1
            found.add(base if not count else f"{base}-{count}")
        if "<" in line:
            for match in NAMED_ANCHOR.finditer(line):
                found.add(html.unescape(match.group(1)))
    anchor_cache[path] = found
    return found


def main() -> int:
    documents = sorted(CORPUS.rglob("*.md"))
    local_links: list[tuple[Path, Path]] = []
    external = 0
    fragments = 0
    parsed_links = 0
    issues: list[str] = []

    for source in documents:
        for number, line in active_lines(source.read_text(encoding="utf-8")):
            destinations = [match.group(1) for match in LINK.finditer(line)]
            ref = REF.match(line)
            if ref:
                destinations.append(ref.group(1))
            if "<" in line:
                destinations += [match.group(1) for match in HTML_LINK.finditer(line)]
            for raw in destinations:
                parsed_links += 1
                raw = html.unescape(raw.strip().strip("<>"))
                parts = urlsplit(raw)
                if parts.scheme or parts.netloc:
                    external += 1
                    continue
                if raw.startswith("//"):
                    external += 1
                    continue
                if not parts.path and not parts.fragment:
                    continue
                if parts.path.startswith("/"):
                    issues.append(f"{source.relative_to(REPO)}:{number}: root-absolute path not validated: {raw}")
                    continue
                target = (source.parent / unquote(parts.path)).resolve() if parts.path else source
                try:
                    target.relative_to(REPO)
                except ValueError:
                    issues.append(f"{source.relative_to(REPO)}:{number}: link escapes repository: {raw}")
                    continue
                if target.is_dir() and parts.fragment:
                    target = target / "README.md"
                if not target.exists():
                    issues.append(f"{source.relative_to(REPO)}:{number}: missing target: {raw}")
                    continue
                local_links.append((source, target))
                if parts.fragment and target.suffix.lower() == ".md":
                    fragments += 1
                    fragment = unquote(parts.fragment)
                    if fragment not in anchors(target):
                        issues.append(f"{source.relative_to(REPO)}:{number}: missing heading fragment: {raw}")
    distinct_targets = len({p for _, p in local_links})
    print(f"Markdown files examined: {len(documents)}")
    print(f"Simple links parsed: {parsed_links}")
    print(f"Internal links resolved: {len(local_links)}")
    print(f"Unique internal targets: {distinct_targets}")
    print(f"Internal fragments checked: {fragments}")
    print(f"External links discovered, not fetched: {external}")
    print(f"Potential link errors: {len(issues)}")
    for issue in issues:
        print(f"ERROR {issue}")
    print("LIMIT: simple Markdown/HTML pattern scan; external URL availability,")
    print("full CommonMark parsing, and claim-to-source accuracy are not checked.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
