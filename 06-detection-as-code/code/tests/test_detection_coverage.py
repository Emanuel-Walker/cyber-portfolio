"""
Detection coverage test harness.

This test suite is the CI gate. It walks every rule in code/rules/ and enforces
three guarantees before a pull request can merge.

1. Every Sigma rule has a matching ADS spec file next to it.
2. The rule matches every event in its paired atomic test (positive coverage).
3. The rule matches zero events in the paired benign fixture (no false positives).

If any guarantee fails, the PR cannot ship. That is the point.
"""

from __future__ import annotations

import pathlib
import re
from typing import Any, Dict, Iterable, List

import pytest
import yaml

# Resolve directories relative to this file. We never hard-code absolute paths
# because the test runs the same way on a laptop and in GitHub Actions.
HERE = pathlib.Path(__file__).resolve().parent
RULES_DIR = HERE.parent / "rules"
ATOMIC_DIR = HERE / "atomic_tests"
BENIGN_DIR = HERE / "benign"


def _load_yaml(path: pathlib.Path) -> Dict[str, Any]:
    """Load a YAML file and return the parsed dictionary.

    We keep this helper so every file goes through the same safe loader.
    Using safe_load means a hostile YAML file cannot instantiate arbitrary
    Python objects on us during CI.
    """
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _get_field(event: Dict[str, Any], field: str) -> str:
    """Return the string value for a dotted field name, or empty string.

    Our test fixtures store fields using dot notation keys ("process.name")
    instead of nested dicts. This matches how Elastic Common Schema is
    rendered in flat JSON documents, which is what a SIEM query actually
    sees. Returning empty string on miss keeps the matcher simple: a
    missing field is just a field with no value, and the "contains" check
    cannot match an empty string.
    """
    value = event.get(field, "")
    return str(value) if value is not None else ""


def _matches_value_list(actual: str, expected: Iterable[str]) -> bool:
    """Case-insensitive equality against any value in a list.

    Sigma lets a selection list multiple acceptable literal values. We
    normalize both sides to lowercase so "powershell.exe" matches
    "PowerShell.exe". Real SIEM backends vary on case sensitivity but
    detection logic should not depend on which one you run.
    """
    actual_lower = actual.lower()
    return any(actual_lower == exp.lower() for exp in expected)


def _matches_endswith(actual: str, expected: Iterable[str]) -> bool:
    """Return True if the actual value ends with any expected suffix.

    Sysmon event data for process paths uses full file paths. The
    "|endswith" modifier in Sigma lets us pin on the executable name
    without caring about the directory. We use this for lsass.exe and
    for EDR agent binaries in the filter list.
    """
    actual_lower = actual.lower()
    return any(actual_lower.endswith(exp.lower()) for exp in expected)


def _matches_contains(actual: str, expected: Iterable[str]) -> bool:
    """Return True if the actual value contains any expected substring.

    PowerShell command lines are long and messy. We match on substrings
    because the attacker-controlled parts of the command line are what
    carry the intent, not the exact shape of the arguments.
    """
    actual_lower = actual.lower()
    return any(exp.lower() in actual_lower for exp in expected)


def _eval_selection(event: Dict[str, Any], selection: Dict[str, Any]) -> bool:
    """Evaluate one Sigma selection block against one event.

    A selection is an AND of its field predicates. Each field predicate can be
    a scalar, a list (OR of literal matches), or a modifier like |contains or
    |endswith. We only implement the modifiers used in this repo. New rules
    that need new modifiers must extend this function and get test coverage
    before they ship.
    """
    for field_spec, expected in selection.items():
        # Pull the modifier off the field name if present.
        if "|" in field_spec:
            field, modifier = field_spec.split("|", 1)
        else:
            field, modifier = field_spec, "equals"

        actual = _get_field(event, field)
        expected_list = expected if isinstance(expected, list) else [expected]

        if modifier == "equals":
            if not _matches_value_list(actual, expected_list):
                return False
        elif modifier == "contains":
            if not _matches_contains(actual, expected_list):
                return False
        elif modifier == "endswith":
            if not _matches_endswith(actual, expected_list):
                return False
        else:
            # Fail loud if a rule uses an unsupported modifier. Silent default
            # behavior would hide bugs where the matcher never actually tested
            # what the rule intended.
            raise ValueError(f"Unsupported Sigma modifier: {modifier}")
    return True


def _eval_condition(condition: str, selections: Dict[str, bool]) -> bool:
    """Evaluate the Sigma condition string using boolean algebra.

    We support the subset of Sigma condition syntax this repo uses:
    AND, OR, NOT, and parentheses. Every rule in this repo should keep its
    condition simple enough to fit. If the project grows, swap this for
    pySigma's parser. For now a hand-rolled evaluator is easier to audit
    and has no third-party dependencies.
    """
    # Replace selection names with their boolean values. We sort by length
    # descending so "selection_cradle" is substituted before "selection"
    # which would otherwise partially-match and corrupt the expression.
    expr = condition
    for name in sorted(selections.keys(), key=len, reverse=True):
        expr = re.sub(rf"\b{re.escape(name)}\b", str(selections[name]), expr)

    # Normalize Sigma keywords into Python keywords. The order matters:
    # replace "and"/"or"/"not" as whole words only, otherwise we would
    # mutilate words like "candidate".
    expr = re.sub(r"\band\b", " and ", expr)
    expr = re.sub(r"\bor\b", " or ", expr)
    expr = re.sub(r"\bnot\b", " not ", expr)

    # eval is safe here because we have already substituted the selection
    # names with True/False literals and the only remaining tokens are
    # Python booleans, operators, and parentheses.
    return bool(eval(expr, {"__builtins__": {}}, {}))


def _rule_matches(rule: Dict[str, Any], event: Dict[str, Any]) -> bool:
    """Return True if the Sigma rule triggers on the event."""
    detection = rule["detection"]
    condition = detection["condition"]
    selections = {
        name: _eval_selection(event, block)
        for name, block in detection.items()
        if name != "condition"
    }
    return _eval_condition(condition, selections)


def _rule_files() -> List[pathlib.Path]:
    """Return every Sigma rule file in the rules directory."""
    return sorted(RULES_DIR.glob("*.yml"))


# ---------- Tests ----------

@pytest.mark.parametrize("rule_path", _rule_files(), ids=lambda p: p.name)
def test_rule_has_ads_spec(rule_path: pathlib.Path) -> None:
    """Every rule ships with an ADS spec next to it. No spec, no merge."""
    ads_path = rule_path.with_suffix(".ads.md")
    assert ads_path.exists(), f"Missing ADS spec: {ads_path.name}"
    # The spec must have real content. An empty file counts as missing.
    assert ads_path.stat().st_size > 500, f"ADS spec too thin: {ads_path.name}"


@pytest.mark.parametrize("rule_path", _rule_files(), ids=lambda p: p.name)
def test_rule_fires_on_positive_atomic(rule_path: pathlib.Path) -> None:
    """Every event in the paired atomic test must trigger the rule."""
    rule = _load_yaml(rule_path)
    rule_stem = rule_path.stem

    # Find the atomic test whose matched_rule points at this rule.
    atomic = None
    for candidate in ATOMIC_DIR.glob("*.yml"):
        data = _load_yaml(candidate)
        if data.get("matched_rule") == rule_stem:
            atomic = data
            break
    assert atomic is not None, f"No atomic test references {rule_stem}"

    # Every event must match. A single miss means the rule has a coverage
    # gap and the author needs to either widen the rule or document the gap
    # as an accepted blind spot in the ADS.
    misses = [
        event["name"]
        for event in atomic["events"]
        if not _rule_matches(rule, event)
    ]
    assert not misses, f"{rule_stem} failed to match atomic events: {misses}"


@pytest.mark.parametrize("rule_path", _rule_files(), ids=lambda p: p.name)
def test_rule_does_not_fire_on_benign(rule_path: pathlib.Path) -> None:
    """No event in any benign fixture may trigger the rule."""
    rule = _load_yaml(rule_path)
    rule_stem = rule_path.stem

    # Benign fixtures are shared across rules. We run every benign file
    # against every rule because a rule that fires on an unrelated benign
    # pattern is also a bug, just a quieter one.
    false_positives = []
    for benign_file in BENIGN_DIR.glob("*.yml"):
        data = _load_yaml(benign_file)
        for event in data["events"]:
            if _rule_matches(rule, event):
                false_positives.append(f"{benign_file.name}:{event['name']}")

    assert not false_positives, (
        f"{rule_stem} fired on benign events: {false_positives}"
    )
