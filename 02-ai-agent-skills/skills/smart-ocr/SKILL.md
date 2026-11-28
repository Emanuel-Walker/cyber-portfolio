---
name: smart-ocr
description: Extract text from images, screenshots, scanned PDFs, photos, handwritten docs using PaddleOCR 3.6 (installed locally, offline after first model download). Routes extracted text to the right folder.
offline: true
requires: [PaddleOCR>=3.6, paddlepaddle, Python 3.12]
---

# Smart OCR (PaddleOCR 3.6)

Extract text from images and scanned documents. Local, offline, no API keys. Model files download on first run (~500 MB to the PaddleX cache). After that, fully offline.

## Install

- `paddleocr` 3.6.x
- `paddlepaddle` 3.3.x
- Python 3.12
- Models cache: `~/.paddlex/` (created on first OCR call, around 500 MB)

If reinstall needed: `pip install --user paddleocr paddlepaddle`

## When to use

- Extract text from screenshots in your inbox or attachments folder
- Read scanned PDFs in your reference folders
- Pull text out of medical, financial, or academic scans
- Capture text from photos (whiteboards, handwritten notes, lecture slides)
- Convert scanned readings or textbooks into searchable Markdown

## When NOT to use

- The PDF is already text-searchable (use `pdftotext` instead)
- The screenshot has selectable text in the source app (paste from source)
- The "image" is actually a markdown render - read the source file
- The user pasted text directly - just read it

## How to invoke

```
/smart-ocr <image-path>                 # Single image, English
/smart-ocr <pdf-path>                   # Scanned PDF to per-page text
/smart-ocr <image-path> lang=ch         # Chinese
/smart-ocr <folder>                     # Batch all images in folder
/smart-ocr <image-path> save=<path>     # Save extracted text to a specific location
```

If no save path is given, inline the extracted text in the response and offer to save to a default folder based on source location.

## Save routing (adapt to your vault)

| Source location | Save extracted text to |
|------------------|------------------------|
| `<your-vault-root>/inbox/Pasted image *.png` | `<your-vault-root>/attachments/screenshots/<YYYY-MM>/<filename>.md` |
| `<your-vault-root>/inbox/<reference PDF>` | `<your-vault-root>/resources/<topic>/<filename>.md` |
| `<your-vault-root>/inbox/<medical PDF>` | `<your-vault-root>/health/records/<filename>.md` |
| `<your-vault-root>/inbox/<academic PDF>` | `<your-vault-root>/academic/<course>/<filename>.md` |
| `<your-vault-root>/inbox/<technical PDF>` | `<your-vault-root>/resources/technical/<filename>.md` |
| `<your-vault-root>/attachments/<existing>` | same folder, `<filename>.ocr.md` alongside |
| Anywhere else | ask user where to save |

Always ask for confirmation before saving to sensitive folders (health, financial, legal).

## Canonical-source rule

If the source is a canonical reference (scripture, legal text, scientific paper), the OCR'd text must not be treated as canonical. OCR introduces small errors (capitalization, punctuation, occasionally word substitution).

Workflow for canonical content:
1. Run OCR.
2. Mark the extracted text as `[OCR'd from <source> - VERIFY AGAINST CANONICAL]`.
3. Surface the specific references for the user to check against the canonical copy.
4. Never use OCR'd text as the primary source in a derivative work. Quote from the canonical copy.
5. If a reference is needed but OCR is the only source: write `[QUOTE: REF - NEED SOURCE]`.

## Workflow

### Step 1: Determine source

Identify what you are OCR'ing:
- Single image (.png, .jpg, .jpeg, .bmp, .tiff, .webp)
- PDF (scanned - image-only, or mixed text and image)
- Folder of images (batch mode)

### Step 2: Determine language

Default: English (`lang='en'`).

Supported language codes (PaddleOCR 3.x):
- `en` - English
- `ch` - Chinese (Simplified)
- `chinese_cht` - Chinese (Traditional)
- `japan` - Japanese
- `korean` - Korean
- `french`, `german`, `spanish`, `russian`, `arabic`, `hindi`, `vi`, `th`

Multi-language: run OCR twice with different `lang=` params and merge by bbox region.

### Step 3: Run OCR (PaddleOCR 3.6 API)

Windows requirement: paddlepaddle 3.3 has an oneDNN compatibility bug on Windows for text-detection ops. Always disable oneDNN with `enable_mkldnn=False` and/or `FLAGS_use_mkldnn=false`.

```python
import os
os.environ['FLAGS_use_mkldnn'] = 'false'   # Windows workaround for paddlepaddle 3.3
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang='en',
    use_textline_orientation=True,          # was use_angle_cls in 2.x
    use_doc_orientation_classify=False,     # skip page-orientation classifier for speed
    use_doc_unwarping=False,                # skip dewarping for speed
    enable_mkldnn=False,                    # required on Windows
)

result = ocr.predict('path/to/image.png')

for res in result:
    res.save_to_img('output_visual.jpg')
    res.save_to_json('output.json')

    rec_texts = res['rec_texts']
    rec_scores = res['rec_scores']
    rec_boxes  = res['rec_boxes']
```

### Step 4: Process result

For each detected line:
- Filter low-confidence reads (default threshold: 0.7)
- Group lines by vertical position (top-to-bottom reading order)
- Preserve paragraph breaks where significant vertical gap exists

### Step 5: Format output

Save extracted text as Markdown with frontmatter:

```markdown
---
title: <source filename without extension>
date: <YYYY-MM-DD>
type: ocr-extract
source: <full path to source image / PDF>
source_type: <image | pdf | screenshot | scan>
ocr_engine: PaddleOCR 3.6
language: en
confidence_average: 0.92
tags: [ocr, <domain tag>]
ocr_warning: true     # for canonical / legal docs - verify before quoting
---

# OCR'd from: <source filename>

> **OCR notice.** This text was extracted by PaddleOCR 3.6. Errors are possible especially in punctuation, capitalization, and handwriting. Verify against the source before quoting.

## Extracted text

<extracted text, paragraph-broken>

## Low-confidence lines (< 0.7)

<list any uncertain reads>

## Source

[[<link to source file in vault>]]
```

### Step 6: Optional debug visualization

If `--debug` requested, save the PaddleOCR visualization alongside (shows bounding boxes on the original image):

```python
res.save_to_img('<source>_ocr_visual.jpg')
```

Useful for verifying region detection on dense pages.

## Batch mode

```python
import os
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en', use_textline_orientation=True)
folder = '<your-vault-root>/attachments/screenshots/YYYY-MM/'

for fname in os.listdir(folder):
    if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
        path = os.path.join(folder, fname)
        result = ocr.predict(path)
        # save to '<fname>.ocr.md' alongside
```

## PDF mode (scanned PDFs)

Use `pypdfium2` (already a PaddleOCR dependency) to rasterize pages first:

```python
import pypdfium2 as pdfium
from paddleocr import PaddleOCR

pdf = pdfium.PdfDocument('path/to/scan.pdf')
ocr = PaddleOCR(lang='en', use_textline_orientation=True)

pages_text = []
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=2.0).to_pil()
    image.save(f'_temp_page_{i}.png')
    result = ocr.predict(f'_temp_page_{i}.png')
    # extract text from result, append to pages_text
    os.remove(f'_temp_page_{i}.png')
```

## Performance notes

| Source | Approx time on CPU |
|--------|---------------------|
| Single 1080p screenshot | 2 to 5 s |
| Page scan (300 DPI) | 5 to 10 s |
| 10-page PDF | 30 to 90 s |
| Batch of 100 images | 5 to 15 min |

First call to `ocr.predict()` is slower (around 30 s) - loads models from disk into memory. Subsequent calls reuse the loaded models.

## Hard rules

1. Never paraphrase OCR'd content. Extract verbatim. If OCR is uncertain, mark it `[?]` or list under "low-confidence lines."
2. Canonical sources are never canonical via OCR. Always verify against the stored canonical copy.
3. Do not overwrite source files. OCR output goes to a sidecar `.ocr.md` file or a routed destination.
4. Confirm save location before writing, especially for sensitive folders.
5. Do not OCR images that already have a markdown sidecar. Check first.
6. No network calls beyond first-run model download. If models are missing, surface the error. Do not auto-download silently.

## Related skills

- `file-organizer` - for sorting OCR'd output into the right folders after extraction
- `obsidian` - for vault save, frontmatter, linkage to source
- `content-engine` - if extracted text is source material for a draft (with canonical-source verification step)
- `humanizer` - never run on OCR'd raw extraction. Only on derivative drafts.
