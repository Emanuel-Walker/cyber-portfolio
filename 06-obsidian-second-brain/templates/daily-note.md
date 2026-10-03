<%*
// Templater syntax. If you do not use Templater, strip the <%* %> blocks and
// replace with static values.
const today = tp.date.now("YYYY-MM-DD");
const dayName = tp.date.now("dddd");
-%>
---
tags:
  - type/daily-note
  - status/draft
created: <% today %>
---

# <% today %> (<% dayName %>)

## Today
- Mood (1-10): 
- Sleep (hours): 
- One thing I will not drop today: 
- One thing I will say no to: 

## Captures

<!-- As the day goes, add timestamped notes here. Example:
## 09:14
Idea for the audit workflow: pull git log too, not just daily notes.
-->

## Evening Close
- What I actually did:
  - 
- What I did not do that I thought I would:
  - 
- Still open:
  - [ ] 
- One line for future me:

## Hyperfixation Meter
**Primary fix today:** 
**Strength:** /10
Notes:

## Agent Note - Session Close
<!-- The agent fills this at session end. Expected shape:
**Date:** <% today %>
**Session type:** [e.g., brain dump + weekly review]
**Files created/updated this session:**
- path/to/file.md - one line
**Key threads to carry forward:**
- [ ] 
_One honest sentence._
-->

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
