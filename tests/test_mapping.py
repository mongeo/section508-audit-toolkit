from a508.mapping import map_results, map_violation, tag_to_sc


def test_tag_to_sc():
    assert tag_to_sc("wcag143") == "1.4.3"
    assert tag_to_sc("wcag1412") == "1.4.12"
    assert tag_to_sc("wcag2aa") is None
    assert tag_to_sc("best-practice") is None


def test_image_alt_maps_to_508_and_tt():
    f = map_violation({"id": "image-alt", "impact": "critical", "tags": ["wcag2a", "wcag111", "section508"],
                       "nodes": [{"target": ["img"]}]})
    assert [c["sc"] for c in f.criteria] == ["1.1.1"]
    assert f.tt_ids == ["6.A"]
    assert f.section508 is True
    assert f.targets == ["img"]


def test_wcag22_target_size_not_in_508():
    f = map_violation({"id": "target-size", "impact": "serious", "tags": ["wcag22aa", "wcag258"], "nodes": []})
    assert f.criteria[0]["name"].startswith("Target Size")
    assert f.section508 is False


def test_best_practice_rule():
    f = map_violation({"id": "region", "impact": "moderate", "tags": ["cat.keyboard", "best-practice"], "nodes": []})
    assert f.criteria == [] and f.best_practice


def test_unknown_sc_is_kept():
    f = map_violation({"id": "x", "tags": ["wcag139"], "nodes": []})
    assert f.criteria[0]["sc"] == "1.3.9" and f.criteria[0]["level"] == "?"


def test_sorted_by_impact():
    res = {"violations": [{"id": "b", "impact": "minor", "tags": []}, {"id": "a", "impact": "critical", "tags": []}]}
    assert [f.rule_id for f in map_results(res)] == ["a", "b"]
