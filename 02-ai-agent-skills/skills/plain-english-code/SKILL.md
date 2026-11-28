---
name: plain-english-code
description: >-
  Use on every code edit: why-comments in plain English, short functions, clear
  names, no clever one-liners, no dead code.
---
# Plain English code

BLUF: Write code a teammate can read once. Comments explain why, not what. Keep functions short and names obvious.

## When to use

Load this whenever you write, edit, or review front end or back end code for an app or site.

## Comments

- Add a short comment above a line or block when the reason is not obvious from the names.
- Comments explain why this exists, why this approach was chosen, or what would break if it changed.
- Write those comments in plain English. Short sentences. Use jargon only when the code already uses it.
- Do not narrate what the next line already says. If a comment only restates the code, delete the comment and improve the name.
- Comment constraints, tradeoffs, security checks, business rules, and workarounds.
- Never leave commented-out code. Delete it.
- Do not leave a TODO that hides unfinished work unless the owner asked to leave a marker. If they did, say what is left and why it waits.

## Shape

- Prefer short functions that do one job.
- Use names that say what the thing is. Avoid abbreviations a new reader would have to guess.
- No clever one-liners that pack several steps into one expression for style points. Split them.
- No dead code, unused imports, unused props, or leftover debug logs.
- Do not invent helpers, flags, or abstractions for a single use.

## No slop

- Match the surrounding file's style and the project's existing patterns.
- Do not add decorative comments, banner art, or emoji.
- Do not write filler comments such as "This function handles the logic for" or "Note that we need to".
- No invented metrics, customers, or comments that claim unproven performance wins.
- UI code still follows the visual no-slop skills. This skill covers the source, not the look.

## How to apply

1. Read the surrounding code before editing.
2. Change only what the task needs.
3. After the edit, reread the diff. Remove dead code. Replace clever lines. Add or trim comments so only why-comments remain.
4. If a comment is doing the work of a better name, rename first.

## QA

A pass means a reviewer can follow the change without a walkthrough, every comment earns its place, and nothing unused remains.
