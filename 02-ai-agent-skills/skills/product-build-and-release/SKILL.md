---
name: product-build-and-release
description: >-
  Use when building or auditing a PDF, workbook, prompt pack, skill, ZIP, or mixed digital product before review or release.
---
# Product build and release

BLUF: Build from editable sources. Verify the actual deliverables. A pass is a review recommendation, not permission to release.

Installed workflow. Verify the selected mode against its output contract.

## Preflight
1. Read the spec, house rules, approved assets, and an existing build script. Freeze the expected file manifest and acceptance tests.
2. Work in a unique private run folder. Record input hashes. Do not edit a shared batch while another actor is writing it. Wait for outputs to settle before auditing.
3. Select build or audit-only mode and the relevant format checks. Never change a source during an audit-only request.

## Build modules
- PDF: retain editable HTML, approved local assets, explicit page breaks, safe margins, readable type, and page numbering. Add a contents page when needed. Render with an available tested renderer. Rasterize every page.
- Workbook: use a deterministic build script and live formulas for computed values. Include an opening guide. Recalculate SAMPLE and BLANK versions. Hand-check sample outputs independently. Test every sheet with blank inputs, zero values, missing matches, duplicate and month-end dates, ties, and boundary cases. Do not call cached values a recalculation test.
- Pack or skill: verify every referenced file and host dependency. Run the instructions as written in the intended host before claiming execution. Test denial paths and unsupported capabilities.
- ZIP: open and extract it. Compare contents to the manifest. Include a one-page how-to-open guide. In build mode, remove stray, hidden, and duplicate files that are not part of the approved package. In audit-only mode, report them without changing the source.

## Release gate
1. Inspect every page or sheet, not a sample presented as full coverage. Check fonts, links, margins, clipping, contrast, page order, duplicate pages, and neighboring pages after edits. Recheck puzzles and answer keys deterministically.
2. Apply the current channel profile, not old thresholds as universal rules. The supplied profile requires white page centers at RGB 252 or above, with permitted cover paper at 251 or above, PDF and ZIP files under 20 MB, and phone-size checks. Confirm interpretation and exceptions against current rules.
3. For listing copy, confirm current platform limits. The supplied profile uses a 140-character title limit and 13 tags of at most 20 characters each. Do not assume these limits apply to another channel.
4. Check copy against the actual files. No invented features, results, ratings, compatibility, counts, or testimonials. Verify quotations and references.
5. Inspect filenames, metadata, embedded text, previews, and manifests for restricted personal material and unapproved marks. Use only current approved branding. Keep internal codenames out.
6. Independently reproduce outside-audit findings. Log path, steps, expected result, actual result, severity, and regression check. After a fix, regenerate and repeat affected tests. Compare hashes and inspect neighboring content.
7. Label evidence OPENED AND INSPECTED, AUTOMATED CHECK, NATIVE APP TESTED, or NOT TESTED. File existence, parsing, rendering, computation, device use, and publication are separate states.

## Output and finish
Deliver the manifest, source and output hashes, test matrix, reproducible defects, and PASS, HOLD, or NEEDS LIVE VALIDATION per file.
Missing or unreadable files remain unverified. Leave the owner decision blank.
Do not upload, list, publish, merge, or change external state without the exact required approval. Preserve the prior release until replacement is authorized.
