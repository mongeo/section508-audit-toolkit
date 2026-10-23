import json
from a508.cli import main
from a508.mapping import map_results
from a508.report import to_html, to_markdown

SAMPLE = {"url": "http://example.test/", "timestamp": "2026-01-01T00:00:00Z", "testEngine": {"version": "4.x"},
          "incomplete": [{}],
          "violations": [{"id": "html-has-lang", "impact": "serious", "help": "<html> needs lang",
                          "helpUrl": "https://dequeuniversity.com/rules/axe/html-has-lang",
                          "tags": ["wcag2a", "wcag311"], "nodes": [{"target": ["html"]}]}]}


def test_markdown_contains_mapping():
    md = to_markdown("u", map_results(SAMPLE), {"incomplete": 1})
    assert "3.1.1 Language of Page (A)" in md and "11.A" in md and "| Yes |" in md


def test_html_escapes():
    out = to_html("<u>", map_results(SAMPLE), {})
    assert "&lt;html&gt; needs lang" in out and 'lang="en"' in out


def test_cli_from_json_and_fail_gate(tmp_path):
    src = tmp_path / "axe.json"
    src.write_text(json.dumps(SAMPLE))
    out = tmp_path / "r"
    assert main(["--from-json", str(src), "--out", str(out)]) == 0
    assert (tmp_path / "r.md").exists() and (tmp_path / "r.html").exists()
    assert main(["--from-json", str(src), "--out", str(out), "--fail-on", "serious"]) == 1
    assert main(["--from-json", str(src), "--out", str(out), "--fail-on", "critical"]) == 0
