#!/usr/bin/env bash
# Scenario 01 runner. Thin wrapper so each scenario has a consistent
# entry point.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
python3 attack.py
