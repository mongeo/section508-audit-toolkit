"""Integration tests: real axe-core scan of the sample pages in headless Chromium."""
from pathlib import Path
import pytest

SAMPLES = Path(__file__).resolve().parent.parent / "samples"


def _scan(name):
    pytest.importorskip("playwright")
    from a508.scanner import scan
    try:
        return scan(SAMPLES.joinpath(name).as_uri())
    except Exception as exc:  # browser not installed
        pytest.skip(f"Chromium unavailable: {exc}")


@pytest.mark.browser
def test_broken_sample_has_violations():
    ids = {v["id"] for v in _scan("broken.html")["violations"]}
    assert {"image-alt", "html-has-lang", "document-title", "button-name"} <= ids


@pytest.mark.browser
def test_fixed_sample_is_clean():
    assert _scan("fixed.html")["violations"] == []
