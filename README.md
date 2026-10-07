---
title: Cyber Portfolio
owner: Emanuel Walker, SEC+, CySA+, SecurityX (CASP+), M.S.
updated: 2026-10-07
---

# Cyber Portfolio

**Emanuel Walker, M.S.**  
Cybersecurity, cloud security, and applied AI.

[Interactive portfolio](https://emanuel-walker-cyber.walkwithemanuel.chatgpt.site) · [Website source](website/)

## What this repo is

I spent six months turning things I was learning and using into working projects.

Some focus on defensive security.

Some focus on using AI without handing it unlimited trust.

One focuses on building a personal knowledge system you actually own.

The common thread is simple:

**build something useful, test it, document the limits, and make it reproducible.**

If you are new here, open:

```text
START_HERE.md
```

## The six projects

### 1. Detection-as-Code

**Problem:** security rules can create noise or miss attacks if nobody tests them before deployment.

**What I built:** a pipeline that treats detection rules like software. Each rule needs a written strategy, a malicious test that must fire, and a normal-use test that must stay quiet.

**Try it:** `01-detection-as-code/QUICKSTART.md`

**Shows:** detection engineering, Python, CI/CD, Sigma, testing.

### 2. Prompt-Injection-Hardened LLM Triage

**Problem:** a SOC AI assistant may read attacker-controlled text inside logs and alerts.

**What I built:** a local alert-triage assistant with input sanitization, strict output validation, provenance logging, and a 16-case adversarial test harness.

The included sample run blocked 12 cases and documented four bypasses.

**Try it:** `02-llm-triage-hardened/QUICKSTART.md`

The first demo is offline. You do not need an LLM installed.

**Shows:** applied AI security, Python, adversarial testing, structured output.

### 3. Crown Jewel Triage

**Problem:** "High severity" does not tell an analyst whether an alert threatens something the business truly depends on.

**What I built:** an asset-centered model that scores critical systems and changes alert priority based on what is at risk.

**Try it:** `03-crown-jewel-triage/QUICKSTART.md`

**Shows:** SOC strategy, risk prioritization, Python, playbooks, business context.

### 4. Identity-First AWS Incident Response Lab

**Problem:** cloud attacks increasingly abuse legitimate identities, roles, and API calls instead of dropping obvious malware.

**What I built:** a disposable AWS lab with intentional identity weaknesses, controlled attack scenarios, GuardDuty comparison testing, and custom detections.

**Try it:** `04-identity-cloud-ir/QUICKSTART.md`

The first demo is offline and free. AWS deployment is optional.

**Shows:** AWS security, Terraform, IAM, CloudTrail, detection engineering, incident response.

### 5. AI Agent Skills

**Problem:** people keep rewriting the same giant prompts for work they repeat every week.

**What I built:** 15 reusable agent skills with clear triggers, scope boundaries, steps, and quality checks.

**Try it:** `05-ai-agent-skills/QUICKSTART.md`

**Shows:** agent design, prompt architecture, workflow automation, technical writing, guardrails.

### 6. Obsidian Second Brain

**Problem:** useful context gets scattered across chats, notes, tabs, and memory.

**What I built:** a local-first Obsidian template with agent charters, reusable workflows, security guidance, ADHD-friendly operating rules, and beginner setup scripts.

**Try it:** `06-obsidian-second-brain/QUICKSTART.md`

**Shows:** knowledge systems, agent orchestration, privacy-aware design, documentation, human-centered AI.

## For hiring managers

If you have five minutes:

1. Read `03-crown-jewel-triage/ESSAY.md`.
2. Open one `QUICKSTART.md`.
3. Read the **What this does not prove** or limitations section.

I care about the third step.

A portfolio should show judgment, not just screenshots.

Resume-ready summaries are in:

```text
RESUME_PROJECTS.md
```

## For builders

Clone the repo:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio
```

Then open:

```text
START_HERE.md
```

Every project should give you:
- a plain-English problem statement
- a short demo
- copy-paste commands
- expected output
- troubleshooting
- an honest limit

## Safety and scope

- All included example data is synthetic.
- Cloud and attack simulations belong in accounts and systems you own or are authorized to test.
- AI model results vary by model and version.
- Local files do not automatically mean local AI processing.
- These projects are demonstrations and engineering artifacts, not production security guarantees.

## About me

I teach what I learn. I write about what I build. I publish what I ship.

- U.S. Army Cyber Warfare Officer
- M.S. Cybersecurity and Information Assurance
- CompTIA Security+, CySA+, SecurityX (CASP+)
- Author of *Unshaken: Finding God's Strength When Life Trembles*

GitHub and LinkedIn are linked from the interactive portfolio.

## Credits

Some projects use or learn from open-source work.

Third-party attribution stays with the relevant project.

AI tools helped with pair-programming and drafting. I own the project choices, testing, claims, and final published work.

## License

MIT unless a project or third-party file says otherwise.
