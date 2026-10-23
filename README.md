# section508-audit-toolkit

A Python command-line tool, `a508`, that scans a page with **axe-core in headless Chromium (playwright-python)**. It then maps each automated finding to:

- **WCAG 2.2 success criteria**, with name and level
- **Revised Section 508** coverage, flagging whether the criterion is part of WCAG 2.0 A/AA, which 508 incorporates by reference, or new in WCAG 2.1/2.2
- **DHS Trusted Tester test IDs**

It writes the results as a **Markdown and HTML audit report**. The repo also includes a **manual audit template** for the checks automation can't do: keyboard, JAWS/NVDA/VoiceOver screen reader checks, visual checks, multimedia, the WCAG 2.2 additions, and linked documents.

## Features
- `a508 --url ...` scans live pages or `file://` pages using the WCAG 2.2 A/AA tag set.
- `a508 --from-json axe.json` re-maps results from any existing axe run (browser extension, CI, and so on).
- `--fail-on serious` returns a nonzero exit code, so the tool can gate CI.
- The HTML report itself is accessible: `lang`, scoped table headers, and a caption.
- The mapping table is plain JSON (`src/a508/data/mapping.json`), so it's easy to review and extend.
- axe-core is bundled (`src/a508/vendor/axe.min.js`, MPL-2.0), so no Node.js is needed.

> **About the Trusted Tester IDs:** the IDs in `mapping.json` are a starting point for triage. Check them against the DHS Trusted Tester Test Process version you certify under before putting them in a formal report. Automated results never replace the manual TT test steps.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
python -m playwright install chromium
a508 --url https://www.example.gov --out reports/example      # writes reports/example.md and .html
a508 --url "file://$PWD/samples/broken.html" --out reports/broken --fail-on serious
pytest -v
```

## Sample output
See [`samples/output/broken-audit.md`](samples/output/broken-audit.md), generated from `samples/broken.html`:

| # | Rule | Impact | WCAG 2.2 SC | Section 508 | Trusted Tester |
|---|---|---|---|---|---|
| 1 | button-name | critical | 4.1.2 Name, Role, Value (A) | Yes | 5.C, 9.A |
| 2 | image-alt | critical | 1.1.1 Non-text Content (A) | Yes | 6.A |
| 4 | color-contrast | serious | 1.4.3 Contrast (Minimum) (AA) | Yes | 7.C |
| 7 | target-size | serious | 2.5.8 Target Size (Minimum) (AA) | No (WCAG 2.1/2.2 only) | - |

![HTML audit report showing summary counts and a findings table mapped to WCAG, Section 508, and Trusted Tester](docs/audit-report.png)

## Manual audit template
[`templates/manual_audit_template.md`](templates/manual_audit_template.md) covers:
- the test environment matrix (JAWS + Chrome, NVDA + Firefox, VoiceOver macOS and iOS)
- keyboard and focus checks, including 2.4.11 Focus Not Obscured
- 12 screen reader checks with a result column for each AT
- visual and sensory, multimedia and timing, the WCAG 2.2 additions, and PDF/Office documents
- an issue log and a conformance summary

## Layout
```
src/a508/  cli.py  scanner.py  mapping.py  report.py  data/mapping.json  vendor/axe.min.js
tests/     unit tests (mapping, report, CLI) + browser integration tests
samples/   broken.html, fixed.html, output/
templates/ manual_audit_template.md
```

## License
MIT © Geoffrey Montague. The bundled axe-core is © Deque Systems under MPL-2.0 (`src/a508/vendor/AXE_LICENSE.txt`).
