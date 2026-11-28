"""
Minimal Sigma to Elastic KQL converter.

We ship our own converter instead of importing pySigma for two reasons.
First, it is small enough to read in one sitting, which means a reviewer can
spot a bad field mapping. Second, every conversion is exercised by the test
suite, so a drift between what the rule claims and what the SIEM would see
gets caught in CI instead of in production.

Usage:
    python sigma_to_elastic.py path/to/rule.yml

Output is printed to stdout. Pipe into a file or into the Elastic Detection
Rules API payload.
"""

from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Any, Dict, Iterable, List

import yaml


# ECS mapping table. The left side is the field name as it appears in a Sigma
# rule in this repo. The right side is the field name as Elastic indexes it.
# We keep the two the same whenever possible because consistency is cheaper
# than cleverness. Entries only appear here when they genuinely differ.
ECS_FIELD_MAP: Dict[str, str] = {
    # Our rules already use ECS field names, so most entries are identity
    # mappings. This dict exists for the cases where a Sigma community rule
    # uses legacy field names like "CommandLine" and we need to normalize.
    "CommandLine": "process.command_line",
    "Image": "process.name",
    "ParentImage": "process.parent.name",
    "User": "user.name",
    "Computer": "host.name",
}


def _normalize_field(field: str) -> str:
    """Translate a Sigma field name into its ECS equivalent.

    If the field is not in the map we return it unchanged. Our rules already
    use ECS names, so the common case is pass-through. The map handles
    imported rules from the Sigma community pack.
    """
    return ECS_FIELD_MAP.get(field, field)


def _kql_quote(value: str) -> str:
    """Return a value quoted for KQL.

    KQL requires double quotes around values that contain spaces or special
    characters. We quote everything to keep the output predictable. The
    only characters we have to escape inside a quoted KQL value are the
    backslash and the double quote itself.
    """
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _render_predicate(field: str, modifier: str, values: Iterable[str]) -> str:
    """Render one Sigma predicate as a KQL fragment.

    A list of values becomes an OR group. Modifiers map as follows:
      equals   -> field: "value"
      contains -> field: *value*
      endswith -> field: *value
    KQL wildcards are supported on keyword fields. If your mapping stores a
    field as text instead of keyword, these wildcards will not work and the
    conversion needs an update.
    """
    normalized = _normalize_field(field)
    parts: List[str] = []
    for raw in values:
        value = str(raw)
        if modifier == "equals":
            parts.append(f"{normalized}: {_kql_quote(value)}")
        elif modifier == "contains":
            # Wildcards inside the value cannot be quoted, so we escape the
            # inner value separately and leave the stars outside the quotes.
            parts.append(f"{normalized}: *{_kql_quote(value)[1:-1]}*")
        elif modifier == "endswith":
            parts.append(f"{normalized}: *{_kql_quote(value)[1:-1]}")
        else:
            raise ValueError(f"Unsupported modifier for KQL rendering: {modifier}")

    # Wrap in parentheses only when the OR group has more than one value,
    # otherwise the output is noisy and reviewers notice the noise before
    # they notice the logic.
    if len(parts) == 1:
        return parts[0]
    return "(" + " or ".join(parts) + ")"


def _render_selection(selection: Dict[str, Any]) -> str:
    """Render an entire selection block as a KQL AND group."""
    fragments: List[str] = []
    for field_spec, value in selection.items():
        if "|" in field_spec:
            field, modifier = field_spec.split("|", 1)
        else:
            field, modifier = field_spec, "equals"
        values = value if isinstance(value, list) else [value]
        fragments.append(_render_predicate(field, modifier, values))
    if len(fragments) == 1:
        return fragments[0]
    return "(" + " and ".join(fragments) + ")"


def _render_condition(condition: str, selection_kql: Dict[str, str]) -> str:
    """Substitute selection names in the condition with their KQL fragments.

    We do textual replacement because Sigma's condition grammar is small and
    the rules in this repo stick to the simple AND/OR/NOT subset. We sort by
    name length descending so longer names substitute before shorter prefixes.
    """
    expr = condition
    for name in sorted(selection_kql.keys(), key=len, reverse=True):
        expr = expr.replace(name, selection_kql[name])
    return expr


def convert(rule_path: pathlib.Path) -> str:
    """Convert a Sigma rule YAML file into a KQL query string."""
    with rule_path.open("r", encoding="utf-8") as fh:
        rule = yaml.safe_load(fh)

    detection = rule["detection"]
    condition = detection["condition"]
    selection_kql = {
        name: _render_selection(block)
        for name, block in detection.items()
        if name != "condition"
    }
    return _render_condition(condition, selection_kql)


def main() -> int:
    """Command-line entry point. Returns an exit code suitable for CI."""
    parser = argparse.ArgumentParser(description="Convert Sigma to Elastic KQL")
    parser.add_argument("rule_path", type=pathlib.Path)
    args = parser.parse_args()

    if not args.rule_path.exists():
        print(f"Rule file not found: {args.rule_path}", file=sys.stderr)
        return 2

    print(convert(args.rule_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
