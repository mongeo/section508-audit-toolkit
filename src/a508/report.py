"""Render mapped findings as Markdown or HTML."""
from __future__ import annotations
import html
from collections import Counter
from .mapping import Finding


def _summary(findings: list[Finding]) -> Counter:
    return Counter(f.impact or "unknown" for f in findings)


def to_markdown(url: str, findings: list[Finding], meta: dict) -> str:
    c = _summary(findings)
    lines = [f"# Automated Accessibility Audit: {url}", "",
             f"- **Scanned:** {meta.get('timestamp', '')}",
             f"- **Engine:** axe-core {meta.get('engine', '')}, WCAG 2.2 A/AA tag set",
             f"- **Violations:** {len(findings)} rules "
             f"({', '.join(f'{k}: {v}' for k, v in sorted(c.items())) or 'none'})",
             f"- **Needs manual review (axe incomplete):** {meta.get('incomplete', 0)}", "",
             "> Automated testing finds only part of the WCAG failures on a page. Use this report alongside the "
             "manual Trusted Tester / screen reader checks in `templates/manual_audit_template.md`.", "",
             "## Findings", "",
             "| # | Rule | Impact | WCAG 2.2 SC | Section 508 | Trusted Tester | Elements |",
             "|---|---|---|---|---|---|---|"]
    for i, f in enumerate(findings, 1):
        sc = "<br>".join(f"{c['sc']} {c['name']} ({c['level']})" for c in f.criteria) or "Best practice"
        s508 = "Yes" if f.section508 else ("No (WCAG 2.1/2.2 only)" if f.criteria else "n/a")
        lines.append(f"| {i} | [{f.rule_id}]({f.help_url}) | {f.impact} | {sc} | {s508} | "
                     f"{', '.join(f.tt_ids) or '-'} | {len(f.targets)} |")
    lines += ["", "## Details", ""]
    for i, f in enumerate(findings, 1):
        lines += [f"### {i}. {f.rule_id}: {f.help}", ""] + [f"- `{t}`" for t in f.targets[:10]] + [""]
    if not findings:
        lines += ["No automated violations detected.", ""]
    return "\n".join(lines)


def to_html(url: str, findings: list[Finding], meta: dict) -> str:
    e = html.escape
    rows = "".join(
        f"<tr><td>{i}</td><td><a href='{e(f.help_url)}'>{e(f.rule_id)}</a><br><small>{e(f.help)}</small></td>"
        f"<td class='imp-{e(str(f.impact))}'>{e(str(f.impact))}</td>"
        f"<td>{'<br>'.join(e(c['sc'] + ' ' + c['name'] + ' (' + c['level'] + ')') for c in f.criteria) or 'Best practice'}</td>"
        f"<td>{'Yes' if f.section508 else ('No, WCAG 2.1/2.2 only' if f.criteria else 'n/a')}</td>"
        f"<td>{e(', '.join(f.tt_ids) or '-')}</td>"
        f"<td><ul>{''.join(f'<li><code>{e(t)}</code></li>' for t in f.targets[:5])}</ul></td></tr>"
        for i, f in enumerate(findings, 1))
    c = _summary(findings)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Accessibility audit: {e(url)}</title><style>
body{{font-family:system-ui,sans-serif;margin:2rem;color:#1b1b1b}}table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #888;padding:.45rem;vertical-align:top;text-align:left}}th{{background:#162e51;color:#fff}}
.imp-critical{{color:#8b0a03;font-weight:bold}}.imp-serious{{color:#a23e00;font-weight:bold}}
.cards{{display:flex;gap:1rem;margin:1rem 0}}.card{{border:1px solid #888;padding:.6rem 1rem;border-radius:6px}}</style></head>
<body><main><h1>Automated Accessibility Audit</h1><p>URL: {e(url)}<br>Scanned: {e(str(meta.get('timestamp','')))}
<br>Engine: axe-core {e(str(meta.get('engine','')))}, WCAG 2.2 A/AA tag set</p>
<div class="cards">{''.join(f'<div class="card"><strong>{v}</strong> {e(k)}</div>' for k, v in sorted(c.items()))}
<div class="card"><strong>{meta.get('incomplete',0)}</strong> need manual review</div></div>
<table><caption class="sr-only">Findings mapped to WCAG, Section 508 and Trusted Tester</caption><thead><tr>
<th scope="col">#</th><th scope="col">Rule</th><th scope="col">Impact</th><th scope="col">WCAG 2.2 SC</th>
<th scope="col">Section 508</th><th scope="col">Trusted Tester</th><th scope="col">Elements</th></tr></thead>
<tbody>{rows or '<tr><td colspan="7">No automated violations detected.</td></tr>'}</tbody></table></main></body></html>"""
