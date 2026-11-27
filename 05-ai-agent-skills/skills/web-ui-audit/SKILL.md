---
name: web-ui-audit
description: Review a website or web UI for accessibility, mobile usability, navigation, interaction clarity, and obvious performance problems. Use for portfolio reviews, UI audits, accessibility checks, or mobile QA.
offline: true
metadata:
  inspiration: vercel-labs/agent-skills web-design-guidelines
---

# Web UI Audit

Review the interface like a real visitor, not only like a developer.

## Audit order

### 1. Can a stranger understand the page?

Within the first screen:
- who is this for?
- what can the visitor do?
- where should they click first?

Flag clever copy that hides the actual purpose.

### 2. Keyboard and focus

Check:
- every interactive element is reachable
- visible focus exists
- dialogs return focus to the opener
- Escape or a clear close action exists
- buttons are buttons, links are links

### 3. Screen reader basics

Check:
- one useful page title
- logical heading order
- form labels
- alt text for informative images
- decorative images hidden from assistive technology
- ARIA only where semantic HTML is insufficient

### 4. Mobile

Check at narrow widths:
- no horizontal scrolling
- tap targets are large enough
- text remains readable
- dialogs fit the viewport
- navigation remains usable
- hover is not required
- important actions stay visible

### 5. Motion

Check:
- animation does not block interaction
- `prefers-reduced-motion` is respected
- important state is not communicated by motion alone

### 6. Content clarity

Every project card should say:
- what it is
- why it matters
- what the visitor can open or run

Avoid tool-name soup.

### 7. Performance basics

Check:
- scripts use `defer` or appropriate module loading
- images have dimensions where practical
- large assets are compressed
- fonts have fallbacks
- no unnecessary third-party scripts
- repeated DOM work is not performed on every scroll

## Output

Use:

```text
BLOCKER
HIGH
MEDIUM
NICE TO HAVE
PASS
```

Give file paths and exact fixes.
