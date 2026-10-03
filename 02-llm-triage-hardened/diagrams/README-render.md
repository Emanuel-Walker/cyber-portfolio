# Rendering the architecture diagram

The source lives in `architecture.drawio`. It is draw.io XML, not a binary.

## Options

1. Open at [https://app.diagrams.net](https://app.diagrams.net), File > Open From > Device, pick `architecture.drawio`.
2. VS Code: install the "Draw.io Integration" extension, open the file in place.
3. Export to PNG from draw.io: File > Export As > PNG. Save next to this README as `architecture.png` if you want it embedded elsewhere.

## What the diagram shows

Left to right: alert JSON enters, the sanitizer cleans and flags it, the
prompt builder wraps it in `<untrusted_field>` delimiters and prepends the
static system prompt, Ollama returns raw text, the output validator either
produces a verdict or rejects on schema drift. Dashed lines go to the
provenance logger, which receives one record per call regardless of outcome.
The attack harness (bottom left, dashed box) feeds poisoned alerts into the
same pipeline and scores results.
