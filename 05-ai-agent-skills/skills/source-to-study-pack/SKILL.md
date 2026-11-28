---
name: source-to-study-pack
description: >-
  Use when converting approved documents, scans, chat exports, or scattered references into searchable Markdown, a study pack, or a source-linked timeline.
---
# Source to study pack

BLUF: Preserve originals and provenance. Make sources easier to retrieve without making them appear more certain.

Installed workflow. Verify the selected mode against its output contract.

## Inputs
Approved files, destination, rights limits, intended audience, and requested output.
Select import, OCR, reference pack, or screenshot timeline. Do not run all modes by default.

## Steps
1. Inventory every supplied file with an ID, format, version, permission, safe locator, and privacy level. Exclude restricted sources and credentials. Keep originals unchanged.
2. Select extraction by type. Use layout-aware PDF text extraction. Pandoc does not read PDF input. Use structural conversion for Office documents. Handle branches and timestamps explicitly for chat JSON.
3. For scans, use local offline OCR. Rasterize scanned PDF pages first. Preserve line order. Compare unclear lines and key values with the original image. OCR is a draft, not proof. Do not upload source images to an online service without permission.
4. Check tables, images, citations, footnotes, page boundaries, and code blocks separately. Flag missing pages, bad characters, unsupported formats, and conflicting versions.
5. Write topic notes with source references and dates. Build INDEX.md. Use tool, concept, and project maps only when useful. Use placeholders instead of unsupported answer values.
6. Dedupe carefully. Preserve conflicts and provenance. Report what was converted, inspected, omitted, or left uncertain.
7. Test retrieval with answerable and unanswerable questions. Require a citation or abstention. State whether a real assistant was tested.
8. Document update and rights limits. Give downstream assistants a small curated context, not the full collection. This is reference preparation, not model training.

## Screenshot timeline mode
Open every screenshot and count coverage. Do not infer content from filenames.
Identify whether each visible time is sent, received, edited, notified, or captured. Never substitute the device clock.
Transcribe legible text exactly. Keep normalized wording in a separate column.
Dedupe overlaps using text, visible time, source, and surrounding sequence. Keep image-to-entry provenance.
Normalize to the requested time zone. Preserve dates and midnight rollover. Mark unknown dates and ordering as uncertain.
Sort by time, then visible sequence for ties. Verify line by line for omissions, duplicates, truncation, and shifted dates.
New batches add corrections with a change log. They must not silently remove verified entries.

## Output and finish
Deliver the manifest, indexed notes or timeline, inspected samples, gaps, and retrieval checks.
Every quotation and answer value must trace to a readable source.
This workflow does not place images into a design. Use verified-visual-production for that.
