---
name: builder-walkthrough
description: Turn a technical project into a beginner build guide with purchases, prerequisites, copy-paste commands, placeholders, checkpoints, troubleshooting, and a clear definition of done.
offline: true
---

# Builder Walkthrough

Use this when a project exists but a normal person still cannot build it.

## Output structure

### 1. What you are building

One paragraph.

No architecture lecture yet.

### 2. What to buy

Separate:
- buy now
- optional later
- do not buy yet

For each item:
- exact product or minimum spec
- quantity
- why it is needed

### 3. What to install

List software before commands.

### 4. Placeholders

Create one table:

| Placeholder | Where to get it |
|---|---|
| `[API_KEY]` | provider dashboard |
| `[DEVICE_IP]` | router/device screen |

### 5. Build steps

One primary action per numbered step.

For every risky step include:
- PASS
- STOP
- cleanup if applicable

### 6. Definition of done

Use observable outcomes.

Bad:

```text
System configured.
```

Good:

```text
Reboot the Pi. The dashboard returns without opening a terminal.
```

### 7. Resume point

Add a status checklist if the build is longer than one sitting.

## Human-effort rule

Prefer:
- wrappers over ten manual commands
- scripts over repetitive file creation
- pinned upstream projects over reimplementing solved problems
- one integration at a time

Do not automate away the checkpoint where the human needs to inspect cost, permissions, or destructive behavior.
