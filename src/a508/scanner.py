"""Run axe-core in Chromium via playwright-python."""
from __future__ import annotations
import json
from importlib import resources

WCAG22_AA_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"]


def axe_source() -> str:
    return resources.files("a508").joinpath("vendor/axe.min.js").read_text()


def scan(url: str, tags: list[str] | None = None, timeout_ms: int = 30000) -> dict:
    from playwright.sync_api import sync_playwright  # imported lazily so unit tests need no browser
    tags = tags or WCAG22_AA_TAGS
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            page = browser.new_page()
            page.goto(url, timeout=timeout_ms, wait_until="load")
            page.add_script_tag(content=axe_source())
            return page.evaluate(
                "async (tags) => await axe.run(document, {runOnly: {type: 'tag', values: tags}})", tags)
        finally:
            browser.close()


def load_results(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)
