# Companion context sync

This folder explains how to keep a daily Companion Agent current without giving it unrestricted access to the full Obsidian vault.

## The model

```text
Obsidian Vault
      |
      v
Vault Agent
      |
      v
99-System/companion/CONTEXT-PACK.md
      |
      v
Companion Agent
```

Examples of companion products might include:

- Muse
- Dot
- ChatGPT
- Claude
- another conversational assistant

This repository does **not** claim every product supports automatic Obsidian sync.

Use the most limited method the product actually supports.

## Method 1 — Manual file upload

Upload:

```text
CONTEXT-PACK.md
```

This is the easiest method to understand and audit.

## Method 2 — Persistent project / knowledge area

If the companion product supports persistent files or project knowledge:

Add only the curated companion context.

Prefer:

```text
ABOUT-ME.md
CURRENT-SEASON.md
PROJECTS.md
COMPANION-RULES.md
CONTEXT-PACK.md
```

Do not upload the whole vault by default.

## Method 3 — Connector

If a legitimate connector exists:

Scope it to the smallest useful folder when possible.

Target:

```text
99-System/companion/
```

Start read-only.

Do not grant write access simply because the connector offers it.

## Method 4 — Copy/paste

Paste the current Context Pack into a conversation.

Boring is acceptable.

Understandable is good.

## Refresh flow

When priorities materially change, tell the Vault Agent:

```text
Refresh 99-System/companion/CONTEXT-PACK.md.

Read only:

99-System/companion/ABOUT-ME.md
99-System/companion/CURRENT-SEASON.md
99-System/companion/PROJECTS.md
99-System/companion/COMPANION-RULES.md

Keep it under 1,500 words.

Do not infer missing facts.

Show me a short summary of what changed.
```

Review the new Context Pack yourself.

Then replace the old companion context.

## Information flowing back into the vault

The companion should produce a:

```text
VAULT CAPTURE
```

You then give that capture to the Vault Agent.

The Vault Agent proposes file changes.

You approve them.

That boundary keeps daily conversation separate from file maintenance.

## Muse / Dot / other companion products

Treat product-specific memory and sync features as adapters.

The architecture should survive if you replace the companion later.

Your durable source of truth remains:

```text
your Obsidian vault
```

Do not design your entire memory system around one companion vendor.
