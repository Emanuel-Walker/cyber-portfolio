# Diagrams

Two draw.io source files live here.

- `triage_flow.drawio` - alert to playbook routing flow
- `asset_tier_pyramid.drawio` - visual of the 6 tiers

## How to render

1. Open https://app.diagrams.net or install the Draw.io desktop app.
2. File > Open > choose the `.drawio` file.
3. Export: File > Export As > PNG or SVG.

For CLI rendering:

```bash
# Requires the drawio-desktop CLI
drawio --export --format png --output triage_flow.png triage_flow.drawio
drawio --export --format png --output asset_tier_pyramid.png asset_tier_pyramid.drawio
```

## What each diagram shows

**triage_flow.** Reads left to right, top to bottom. Alert enters, asset lookup, 4-factor score, type-based routing, priority math, queue, playbook routing, human action, metrics. Blue nodes are input and lookup. Green is scoring. Yellow is routing. Red is output to humans. Purple is feedback to the dashboard.

**asset_tier_pyramid.** Reads top to bottom. Tier 1 is at the top because it has the fewest assets and the highest value per alert. The pyramid widens as you descend because every tier below holds more assets than the one above. Attackers climb the pyramid. Defenders watch the top.
