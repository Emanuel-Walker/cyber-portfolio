#!/usr/bin/env python3
"""
crown_jewel_scorer.py

Why this exists:
    An alert on your payment processor should outrank a High on a marketing
    laptop. The SIEM does not know that. This script does.

How it works:
    1. Load an asset inventory (YAML).
    2. Load one or more alerts (JSON on stdin, single --alert file, or JSONL).
    3. For each alert: look up the asset, grab its tier, compute a priority
       score (severity_base * tier_multiplier).
    4. Print a sorted result.

Why these inputs:
    YAML for the inventory because humans will hand-edit it until there is a
    CMDB integration. JSON for alerts because that is what every SIEM ships.

Usage:
    python3 crown_jewel_scorer.py --inventory example_asset_inventory.yaml \
        --alert single_alert.json
    python3 crown_jewel_scorer.py --inventory example_asset_inventory.yaml \
        --alerts example_alerts.jsonl
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# Load the rubric from the models directory. Keeping it in YAML instead of
# hardcoded in Python means a non-engineer can tune the scoring without
# touching code.
RUBRIC_PATH = Path(__file__).parent / "models" / "scoring_rubric.yaml"


def load_rubric(path=RUBRIC_PATH):
    """Load the scoring rubric.

    The rubric defines severity_base values, tier multipliers, and the score
    bands that map a 4-20 total score to a tier. We load this at runtime so
    tuning the rubric does not require a code change.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_inventory(path):
    """Load the asset inventory YAML into a dict keyed by asset_id.

    Keying by asset_id up front means every alert lookup is O(1). The
    inventory file is small enough that we do not need anything fancier.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    inventory = {}
    for asset in data.get("assets", []):
        inventory[asset["asset_id"]] = asset
    return inventory


def compute_tier(asset, rubric):
    """Compute an asset's tier from its four factor scores.

    Why we do this on the fly instead of trusting a hand-set tier:
    Humans forget to update the cj_tier field after they edit a score.
    Recomputing from the raw scores every run is cheap and keeps the data
    honest. The YAML comments next to each asset are notes for humans, not
    truth for the engine.

    Tier routing has two layers:
    1. Score band (sum of the four 1-5 factors, so 4 to 20).
    2. Asset type override (an identity system in the top band always routes
       to tier 2 regardless of exact score, because the playbook is different
       from a payment system).

    This function returns the numeric tier only. Type-based routing happens
    one level up when we select a playbook.
    """
    scores = asset.get("scores", {})
    total = sum(scores.get(k, 0) for k in
                ["business_impact", "data_sensitivity", "blast_radius", "recovery_cost"])

    # Walk the bands in the rubric. Order matters: we check highest first
    # because tier 1 is the loudest and we would rather over-tier than under.
    if total >= 18:
        return 1
    if total >= 15:
        # Score band 15-17 could be tier 2 or 3 depending on asset type.
        # Default to tier 3 (build/deploy). The run_prioritization step
        # does the asset-type override.
        return 3
    if total >= 11:
        return 4
    if total >= 8:
        return 5
    return 6


def route_tier(asset, numeric_tier):
    """Apply asset-type overrides to turn a numeric tier into a playbook tier.

    Why we need this:
    A payment system and an SSO tenant can both score 19. They are both
    tier 1 by the numbers. But the playbook for payment is very different
    from the playbook for identity. We route by what the asset IS, not just
    what it scored.
    """
    name = asset.get("name", "").lower()
    biz = asset.get("business_function", "").lower()

    # Identity / auth systems get the identity playbook even if they would
    # otherwise be tier 1 by score. The score tells us how much we care; the
    # type tells us which playbook to run.
    identity_markers = ["sso", "okta", "idp", "identity", "aws-admin", "cloud admin",
                        "entra", "azure ad", "ad-domain"]
    if any(m in name or m in biz for m in identity_markers):
        if numeric_tier <= 3:
            return 2

    # Build / deploy systems get the supply chain playbook.
    build_markers = ["jenkins", "ci", "build", "artifactory", "registry",
                     "github-actions", "gitlab-runner"]
    if any(m in name or m in biz for m in build_markers):
        if numeric_tier <= 3:
            return 3

    # Lateral stepping stones. Jump hosts, bastions, VPN.
    lateral_markers = ["jump", "bastion", "vpn", "proxy"]
    if any(m in name or m in biz for m in lateral_markers):
        return 5

    # SaaS data path (regulated data egress).
    saas_regulated = (asset.get("data_classification") == "regulated"
                      and asset.get("cloud_provider", "").startswith("saas"))
    if saas_regulated and numeric_tier in (3, 4):
        return 4

    return numeric_tier


def score_alert(alert, inventory, rubric):
    """Score a single alert.

    Why this math (severity_base * tier_multiplier):
    We want tier to dominate. A Medium on tier 1 (4 * 10 = 40) should beat
    a High on tier 6 (7 * 1 = 7). Multiplicative scoring makes that happen
    without a bunch of if/else cases.
    """
    asset_id = alert.get("asset_id")
    asset = inventory.get(asset_id)

    severity = alert.get("severity", "medium").lower()
    severity_base = rubric["severity_base"]["values"].get(severity, 4)

    if asset is None:
        # Unknown asset. We do not know what it is worth, so we default to
        # tier 5 (lateral) because that is the most dangerous bucket to
        # under-tier. Better to over-investigate than to miss movement.
        tier = 5
        tier_source = "unknown-asset-default"
    else:
        numeric = compute_tier(asset, rubric)
        tier = route_tier(asset, numeric)
        tier_source = f"scored-tier-{numeric}-routed-to-{tier}"

    multiplier = rubric["tier_multipliers"]["values"].get(tier, 1.0)
    priority = severity_base * multiplier

    return {
        "alert_id": alert.get("alert_id"),
        "asset_id": asset_id,
        "asset_name": asset.get("name") if asset else "UNKNOWN",
        "detection_name": alert.get("detection_name"),
        "severity": severity,
        "tier": tier,
        "tier_source": tier_source,
        "priority_score": round(priority, 2),
        "summary": alert.get("summary", ""),
    }


def load_alerts(args):
    """Load alerts from --alert (single JSON) or --alerts (JSONL)."""
    if args.alert:
        with open(args.alert, "r", encoding="utf-8") as f:
            return [json.load(f)]
    if args.alerts:
        alerts = []
        with open(args.alerts, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                alerts.append(json.loads(line))
        return alerts
    # Fall back to stdin for pipeline use.
    if not sys.stdin.isatty():
        return [json.loads(sys.stdin.read())]
    raise SystemExit("No alert source. Use --alert, --alerts, or pipe JSON on stdin.")


def main():
    parser = argparse.ArgumentParser(description="Crown Jewel Triage alert scorer.")
    parser.add_argument("--inventory", required=True, help="Path to asset inventory YAML.")
    parser.add_argument("--alert", help="Path to a single JSON alert.")
    parser.add_argument("--alerts", help="Path to a JSONL file of alerts.")
    parser.add_argument("--rubric", default=str(RUBRIC_PATH), help="Path to scoring rubric YAML.")
    args = parser.parse_args()

    rubric = load_rubric(args.rubric)
    inventory = load_inventory(args.inventory)
    alerts = load_alerts(args)

    results = [score_alert(a, inventory, rubric) for a in alerts]
    # Sort by priority_score descending. Highest priority first is the whole
    # point of this exercise.
    results.sort(key=lambda r: r["priority_score"], reverse=True)

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
