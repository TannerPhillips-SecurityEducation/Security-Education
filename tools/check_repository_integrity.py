#!/usr/bin/env python3
"""Repository-wide Markdown/link and scoped AGENTS contract integrity.

Mechanical checks only; never asserts source accuracy, semantic completeness,
expert review, article approval or publication. Inventory counts are dynamic.
"""
from __future__ import annotations
import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
FENCE=re.compile(r"^ {0,3}(\x60{3,}|~{3,})")
HEADING=re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")
INLINE=re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)")
REFERENCE=re.compile(r"^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)")
HTML_URL=re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']",re.I)
NAMED_ANCHOR=re.compile(r"\b(?:id|name)\s*=\s*[\"']([^\"']+)[\"']",re.I)

def active_lines(source):
    char,size=None,0
    for n,line in enumerate(source.splitlines(),1):
        m=FENCE.match(line)
        if m:
            fence=m.group(1)
            if char is None: char,size=fence[0],len(fence)
            elif char==fence[0] and len(fence)>=size: char,size=None,0
            continue
        if char is None: yield n,line

def slug(title):
    title=re.sub(r"<[^>]+>","",title)
    title=re.sub(r"!?\[([^\]]*)\]\([^)]*\)",r"\1",title)
    title=html.unescape(title).replace(chr(96),"").replace("*","").replace("~","")
    return re.sub(r"[^\w\- ]","",title.lower().strip()).replace(" ","-")

CACHE={}
def anchors(path):
    if path in CACHE: return CACHE[path]
    seen,result={},set()
    for _,line in active_lines(path.read_text(encoding="utf-8")):
        m=HEADING.match(line)
        if m:
            base=slug(m.group(1));n=seen.get(base,0)
            result.add(base if n==0 else f"{base}-{n}");seen[base]=n+1
        for m in NAMED_ANCHOR.finditer(line):
            result.add(html.unescape(m.group(1)))
    CACHE[path]=result
    return result

def main():
    docs=sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.relative_to(ROOT).parts)
    errors=[];links=fragments=external=0
    for doc in docs:
        for number,line in active_lines(doc.read_text(encoding="utf-8")):
            destinations=[m.group(1) for m in INLINE.finditer(line)]
            ref=REFERENCE.match(line)
            if ref: destinations.append(ref.group(1))
            destinations.extend(m.group(1) for m in HTML_URL.finditer(line))
            for dest in destinations:
                dest=html.unescape(dest.strip().strip("<>"))
                parts=urlsplit(dest)
                if parts.scheme or parts.netloc or dest.startswith("//"):
                    external+=1;continue
                if not parts.path and not parts.fragment: continue
                if parts.path.startswith("/"):
                    errors.append(f"{doc.relative_to(ROOT)}:{number}: absolute link: {dest}");continue
                target=(doc.parent/unquote(parts.path)).resolve() if parts.path else doc
                try: target.relative_to(ROOT)
                except ValueError:
                    errors.append(f"{doc.relative_to(ROOT)}:{number}: repository escape: {dest}");continue
                if target.is_dir(): target=target/"README.md"
                if not target.is_file():
                    errors.append(f"{doc.relative_to(ROOT)}:{number}: missing file: {dest}");continue
                links+=1
                if parts.fragment and target.suffix==".md":
                    fragments+=1
                    if unquote(parts.fragment) not in anchors(target):
                        errors.append(f"{doc.relative_to(ROOT)}:{number}: missing fragment: {dest}")
    if not (ROOT/"AGENTS.md").is_file(): errors.append("Missing root AGENTS.md")
    top=[]
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name!=".git" and ((d/"README.md").is_file() or d.name==".github"):
            top.append(d.name)
            if not (d/"AGENTS.md").is_file():
                errors.append(f"Missing top-level instruction contract: {d.name}/AGENTS.md")
    sub=[]
    base=ROOT/"foundations"
    if base.is_dir():
        for d in sorted(base.iterdir()):
            if d.is_dir() and (d/"README.md").is_file():
                sub.append(d.name)
                if not (d/"AGENTS.md").is_file():
                    errors.append(f"Missing division contract: {d.relative_to(ROOT)}/AGENTS.md")
    print(f"MARKDOWN_FILES={len(docs)}")
    print(f"INTERNAL_LINKS_RESOLVED={links}")
    print(f"INTERNAL_FRAGMENTS_CHECKED={fragments}")
    print(f"EXTERNAL_URL_OCCURRENCES_NOT_FETCHED={external}")
    print(f"TOP_LEVEL_CONTRACTS={len(top)}")
    print(f"FOUNDATION_DIVISION_CONTRACTS={len(sub)}")
    print(f"REPOSITORY_INTEGRITY_ERRORS={len(errors)}")
    for e in errors: print("ERROR "+e)
    print("LIMIT: links/contracts only, not semantic accuracy, source verification or publication.")
    return 1 if errors else 0

if __name__=="__main__": sys.exit(main())
