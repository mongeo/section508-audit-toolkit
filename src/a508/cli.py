"""a508 command-line interface."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .mapping import map_results
from .report import to_html, to_markdown
from .scanner import load_results, scan


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="a508", description="WCAG 2.2 / Section 508 automated audit")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="page URL to scan (http(s):// or file://)")
    src.add_argument("--from-json", help="existing axe-core results JSON to map")
    ap.add_argument("--format", choices=["md", "html", "both"], default="both")
    ap.add_argument("--out", default="audit-report", help="output path without extension")
    ap.add_argument("--save-raw", action="store_true", help="also save raw axe JSON")
    ap.add_argument("--fail-on", choices=["none", "minor", "moderate", "serious", "critical"], default="none",
                    help="exit 1 if a violation at this impact or worse exists (CI gate)")
    a = ap.parse_args(argv)

    results = scan(a.url) if a.url else load_results(a.from_json)
    url = a.url or results.get("url", a.from_json)
    findings = map_results(results)
    meta = {"timestamp": results.get("timestamp", ""), "engine": results.get("testEngine", {}).get("version", ""),
            "incomplete": len(results.get("incomplete", []))}
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if a.format in ("md", "both"):
        out.with_suffix(".md").write_text(to_markdown(url, findings, meta), encoding="utf-8")
    if a.format in ("html", "both"):
        out.with_suffix(".html").write_text(to_html(url, findings, meta), encoding="utf-8")
    if a.save_raw:
        out.with_suffix(".axe.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"{len(findings)} violation rule(s) -> {out}.[md|html]")
    order = ["minor", "moderate", "serious", "critical"]
    if a.fail_on != "none":
        threshold = order.index(a.fail_on)
        if any(f.impact in order and order.index(f.impact) >= threshold for f in findings):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
