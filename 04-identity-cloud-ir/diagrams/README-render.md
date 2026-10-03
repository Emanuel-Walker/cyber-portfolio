# Rendering the diagrams

Three `.drawio` files in this folder:

- `lab_architecture.drawio` - what Terraform builds
- `attack_scenarios.drawio` - flow of the 5 attack scenarios
- `detection_coverage_matrix.drawio` - visual version of the matrix

## Option 1: open in diagrams.net (web, free, no account)

1. Go to https://app.diagrams.net.
2. "Open Existing Diagram" -> pick the `.drawio` file.
3. File -> Export As -> PNG. Pick 2x scale.

## Option 2: VS Code extension

Install `hediet.vscode-drawio`. Open the file. It renders inline. Right-click -> Export.

## Option 3: CLI (headless)

```bash
# needs the drawio desktop app installed
drawio --export --format png --scale 2 lab_architecture.drawio
drawio --export --format png --scale 2 attack_scenarios.drawio
drawio --export --format png --scale 2 detection_coverage_matrix.drawio
```

The exported PNGs are suitable for README embeds. Keep the `.drawio` source checked in, treat PNGs as derived artifacts.
