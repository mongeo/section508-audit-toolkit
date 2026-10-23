"""Map axe-core results to WCAG 2.2 success criteria, Section 508, and Trusted Tester IDs."""
from __future__ import annotations
import json
import re
from dataclasses import dataclass, field
from importlib import resources

_TAG = re.compile(r"^wcag(\d)(\d)(\d+)$")
IMPACT_ORDER = {"critical": 0, "serious": 1, "moderate": 2, "minor": 3, None: 4}


def load_mapping() -> dict:
    return json.loads(resources.files("a508").joinpath("data/mapping.json").read_text())


def tag_to_sc(tag: str) -> str | None:
    """'wcag143' -> '1.4.3'; 'wcag1412' -> '1.4.12'; non-SC tags -> None."""
    m = _TAG.match(tag)
    return f"{m.group(1)}.{m.group(2)}.{m.group(3)}" if m else None


@dataclass
class Finding:
    rule_id: str
    impact: str | None
    help: str
    help_url: str
    criteria: list[dict] = field(default_factory=list)
    targets: list[str] = field(default_factory=list)
    best_practice: bool = False

    @property
    def tt_ids(self) -> list[str]:
        return sorted({t for c in self.criteria for t in c["tt"]})

    @property
    def section508(self) -> bool:
        # 508 incorporates WCAG 2.0 A/AA; 2.1/2.2-only criteria are flagged separately.
        return any(c.get("in_508") for c in self.criteria)


def _wcag20_sc(sc: str) -> bool:
    new_in_21_22 = {"1.3.4", "1.3.5", "1.3.6", "1.4.10", "1.4.11", "1.4.12", "1.4.13", "2.1.4",
                    "2.4.11", "2.4.12", "2.4.13", "2.5.1", "2.5.2", "2.5.3", "2.5.4", "2.5.7", "2.5.8",
                    "3.2.6", "3.3.7", "3.3.8", "4.1.3"}
    return sc not in new_in_21_22


def map_violation(v: dict, mapping: dict | None = None) -> Finding:
    mapping = mapping or load_mapping()
    crit = []
    for sc in sorted({s for s in (tag_to_sc(t) for t in v.get("tags", [])) if s}):
        info = mapping["wcag"].get(sc, {"name": "(not in local table)", "level": "?", "tt": []})
        crit.append({"sc": sc, "name": info["name"], "level": info["level"], "tt": info["tt"],
                     "in_508": _wcag20_sc(sc) and info["level"] in ("A", "AA")})
    return Finding(
        rule_id=v["id"], impact=v.get("impact"), help=v.get("help", ""), help_url=v.get("helpUrl", ""),
        criteria=crit, targets=[" ".join(map(str, n.get("target", []))) for n in v.get("nodes", [])],
        best_practice="best-practice" in v.get("tags", []) and not crit,
    )


def map_results(axe_results: dict) -> list[Finding]:
    mapping = load_mapping()
    out = [map_violation(v, mapping) for v in axe_results.get("violations", [])]
    return sorted(out, key=lambda f: (IMPACT_ORDER.get(f.impact, 4), f.rule_id))
