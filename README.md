---
title: Cyber Portfolio
owner: Emanuel Walker, SEC+, CySA+, SecurityX (CASP+), M.S.
updated: 2026-10-03
---

# Cyber Portfolio

**Emanuel Walker, SEC+, CySA+, SecurityX (CASP+), M.S.**
Cyber + CloudSec + AI Builder

Four projects. One answer to "what do you actually do."

I build detection content, triage tooling, SOC operating models, and cloud IR labs. Every project here is runnable, honestly limited, and documented like a blog post I would want to read.

## The four

### 1. Detection-as-Code with Discipline
`01-detection-as-code/`

Sigma rules shipped like software. Every rule gets a written spec, a positive test, a benign test, and a CI gate. The pipeline fails if the rule misses what it claims to catch or fires on things it should not.

**You read this if:** you want to see what detection engineering looks like when it's a program, not a hobby.

**Resume line:** Built a CI/CD pipeline for Sigma rules with Palantir ADS specs and dual-gated tests. Positive detection tests and benign non-fire tests both block merge. Converts to Elastic, Splunk, and Panther on green.

### 2. Prompt-Injection-Hardened LLM Triage
`02-llm-triage-hardened/`

A local Ollama triage agent for SOC alerts. Then an attack harness I built against my own agent. 12 out of 16 injections blocked. 4 still slip through. Named, explained, honest. Companion engineering to "The Agent on the Desk" (Gray Space, June 2026).

**You read this if:** you want to see what hardening an LLM for defensive work actually looks like, and what still breaks.

**Resume line:** Shipped a local LLM triage assistant with structured I/O, output schema validation, provenance logging, and a 16-payload prompt-injection test harness. Documented the four bypasses still open and why.

### 3. Crown Jewel Triage
`03-crown-jewel-triage/`

The signature piece. Civilian SOCs prioritize alerts by severity dropdown. The result is burnout and buried breaches. This repo rebuilds triage around the assets attackers actually want. Score your crown jewels, route alerts by what they threaten, run tier-based playbooks instead of alert-type playbooks.

**You read this if:** you want to see a working alternative to severity-based triage.

**Resume line:** Designed and shipped an asset-tied alert prioritization model with a four-factor scoring rubric, six tier-based response playbooks, a Grafana dashboard for tier-grouped SLA tracking, and a standalone essay on why severity-based triage burns teams out.

### 4. Identity-First AWS Incident Response Lab
`04-identity-cloud-ir/`

Terraform spins up a cloud environment with real identity weaknesses. Five attack scripts hit it. GuardDuty catches some. Custom detections catch what GuardDuty misses. Scattered Spider tabletop included. Costs under five dollars end to end if you remember to run `terraform destroy`.

**You read this if:** you want to see what cloud detection looks like when identity is the attack surface.

**Resume line:** Built a Terraform-deployed AWS IR lab with five identity-centric attack scenarios, matched detections across GuardDuty, Elastic, and Panther, and a Scattered Spider tabletop. Documented the specific GuardDuty gaps the custom rules close.

### 5. AI Agent Skills
`05-ai-agent-skills/`

Ten modular skill files that teach AI assistants how to do specialized work. Content generation, voice calibration, diagram authoring, OCR, prompt optimization, more. Each one adapted from my own workflow. Fork what works.

**You read this if:** you want to see what prompt engineering looks like when it's organized into reusable modules instead of one giant system prompt.

**Resume line:** Published 10 modular skill files for AI assistants covering content generation, voice calibration, diagram authoring, OCR, prompt optimization, and more. Each skill scoped with trigger conditions, scope boundaries, and output contracts.

### 6. Obsidian Second Brain Template
`06-obsidian-second-brain/`

A template for running Obsidian as a second brain with any AI agent (Claude Code, Codex, Hermes, Cursor). PARA structure, 8 ready templates, 6 workflows, 5 security guides, agent setup files, and an ADHD guide. Built for busy professionals and security people who want local-first thinking with a thought partner.

**You read this if:** you want to see what a working second brain + AI thought partner setup actually looks like, security included.

**Resume line:** Published an open-source Obsidian second-brain template with agent-ready instructions (Claude Code, Codex, Hermes), 8 Obsidian templates, 6 workflows, 5 security guides covering local-first setup through encrypted sync, and a dedicated ADHD guide.

## How to read this portfolio

Every project has a `QUICKSTART.md` with a 5-minute demo. Start there if you want to see something run before you read the writeup.

If you want to actually run something, every project has a QUICKSTART. Project 6 has a full WALKTHROUGH that starts from installing Obsidian.

Start with whichever project speaks to the role you're hiring for. Each project has its own README that tells you what to run first. None of these need a cluster or a lab setup. A laptop and an afternoon are enough.

## What this is not

- Not a toolkit for sale
- Not a certification cram
- Not an advertisement for a service
- Not a thought-leadership deck

It's a set of real things I built and the writeups I wish existed when I was learning.

## About the work

All synthetic data. All fictional scenarios. All code runs locally or in a sandboxed cloud account. No real org names, no real IPs, no real customer data.

## About me

I teach what I learn. I write about what I build. I publish what I ship.

- **Author of *Unshaken*** - a book on faith, resilience, and formation under pressure.
- **"The Agent on the Desk,"** Gray Space, June 2026. An essay on AI as both tool and risk on the operator's desk. Project 2 in this repo is the engineering follow-up.
- **M.S., Cybersecurity and Information Assurance,** Western Governors University, 2026.
- **Certifications:** CompTIA Security+, CySA+, SecurityX (CASP+).
- **Writing cadence:** essays on detection engineering, cloud security, and AI-in-the-loop defense. Reach out if a piece in this repo sparks something.
- **Also on my GitHub:** *Good Deeds Coin* - a cryptocurrency project I shipped before the AI boom. Receipt for building ahead of the wave.

## For hiring managers

If you want to see how I think, read `03-crown-jewel-triage/ESSAY.md` first. It is a short piece on why severity-based triage is burning out your SOC and what to replace it with. The rest of the repo shows what the fix looks like in code.

If you want to see how I ship, open any project folder. Every one has a README, a technical writeup, runnable code, and an honest "what I learned" section. No vaporware.

## For LinkedIn

Feel free to copy any of the resume lines above into your own evaluation notes. If you link this repo to a candidate review, mention the project that caught your attention. I like knowing which lane is working.

## Credits

Pair-programmed with Claude Code. The brand, the voice, and the opinions are mine. The semicolons it keeps trying to add are not.

## License

MIT. Use it, remix it, teach from it.
