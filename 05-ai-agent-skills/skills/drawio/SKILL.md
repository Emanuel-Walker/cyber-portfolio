---
name: drawio
description: Create and edit draw.io diagrams in XML format. Use when the user wants to create flowcharts, architecture diagrams, sequence diagrams, or any visual diagrams. Handles XML structure, styling, fonts, arrows, connectors, and PNG export.
---

# Draw.io Diagram Skill

Create and edit draw.io files (`.drawio`) directly in XML.

## Base XML structure

```xml
<mxfile host="app.diagrams.net" modified="2024-01-01T00:00:00.000Z" agent="Claude" version="21.0.0">
  <diagram name="Page-1" id="page-1">
    <mxGraphModel dx="1000" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0" defaultFontFamily="Helvetica">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- shape elements go here -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## mxCell elements

### Rectangle

```xml
<mxCell id="rect-1" value="Label" style="rounded=0;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=18;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry" />
</mxCell>
```

### Rounded rectangle

```xml
<mxCell id="rounded-1" value="Label" style="rounded=1;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=18;arcSize=20;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry" />
</mxCell>
```

### Ellipse

```xml
<mxCell id="ellipse-1" value="Label" style="ellipse;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=18;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="80" as="geometry" />
</mxCell>
```

### Diamond

```xml
<mxCell id="diamond-1" value="Condition" style="rhombus;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=18;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="100" height="100" as="geometry" />
</mxCell>
```

### Text only

```xml
<mxCell id="text-1" value="Text" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Helvetica;fontSize=18;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="30" as="geometry" />
</mxCell>
```

## Arrows and connectors

### Basic arrow

```xml
<mxCell id="arrow-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontFamily=Helvetica;fontSize=14;" edge="1" parent="1" source="rect-1" target="rect-2">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### Labeled arrow

```xml
<mxCell id="arrow-2" value="Label" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontFamily=Helvetica;fontSize=14;" edge="1" parent="1" source="rect-1" target="rect-2">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### Dashed arrow

```xml
<mxCell id="arrow-3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;fontFamily=Helvetica;fontSize=14;" edge="1" parent="1" source="rect-1" target="rect-2">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

## Styling guide

### Font (required)

1. Set `defaultFontFamily="Helvetica"` on `mxGraphModel` (or your preferred font).
2. Add `fontFamily=Helvetica;` explicitly to every text element.

### Recommended settings

| Item | Recommended | Why |
|------|-------------|-----|
| fontSize | 18 | 1.5x standard, better readability |
| Text width | 10 to 20 px per character | Layout calculation |
| Arrow and label spacing | 20px minimum | Prevent overlap |

### Colors

```text
fillColor=#ffffff;      # fill color
strokeColor=#000000;    # border color
fontColor=#333333;      # text color
```

### Common colors

| Use | Hex |
|-----|-----|
| White background | #ffffff |
| Light blue | #dae8fc |
| Light green | #d5e8d4 |
| Light yellow | #fff2cc |
| Light red | #f8cecc |
| Light gray | #f5f5f5 |

## Placement rules

### XML order equals draw order

- Elements written earlier render to the back.
- Arrows go before shapes in XML so they sit behind shapes.

### Recommended structure

```xml
<root>
  <mxCell id="0" />
  <mxCell id="1" parent="0" />

  <!-- 1. Arrows and connectors (back) -->
  <mxCell id="arrow-1" ... edge="1" ... />
  <mxCell id="arrow-2" ... edge="1" ... />

  <!-- 2. Shapes (middle) -->
  <mxCell id="rect-1" ... vertex="1" ... />
  <mxCell id="rect-2" ... vertex="1" ... />

  <!-- 3. Text labels (front) -->
  <mxCell id="text-1" ... vertex="1" ... />
</root>
```

## PNG export

### drawio-export command (recommended for headless)

In Docker or server environments, use `drawio-export` via xvfb:

```bash
drawio-export -x -f png -s 2 -t -o output.png input.drawio
```

### drawio CLI (direct)

With a display environment:

```bash
drawio -x -f png -s 2 -t -o output.png input.drawio
```

### Options

| Option | Description |
|--------|-------------|
| -x | Export mode |
| -f png | PNG format (also svg, pdf, vsdx) |
| -s 2 | 2x scale (high resolution) |
| -t | Transparent background |
| -o | Output file |
| -p | Page number (0-indexed) |
| -b | Border size |

### Examples

```bash
# Basic PNG
drawio-export -x -f png -o diagram.png diagram.drawio

# High-resolution plus transparent background
drawio-export -x -f png -s 2 -t -o diagram@2x.png diagram.drawio

# SVG
drawio-export -x -f svg -o diagram.svg diagram.drawio

# All pages to one PDF
drawio-export -x -f pdf -o diagram.pdf diagram.drawio
```

## Validation checklist

After creating a diagram, check:

- [ ] `defaultFontFamily` set on `mxGraphModel`
- [ ] Every text element has an explicit `fontFamily`
- [ ] `fontSize` around 18 for readability
- [ ] Arrows placed earlier in XML than shapes (back layer)
- [ ] At least 20px between arrows and labels
- [ ] Text width scales with character count
- [ ] PNG export checked visually

## Template

A minimal starter template is in `references/templates/basic.drawio`.
