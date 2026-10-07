# Resume project guide

These bullets are written so a technical recruiter, hiring manager, or interviewer can understand the outcome without already knowing the tool names.

Use the shorter version on a one-page resume. Use the expanded version on LinkedIn or a project portfolio.

## 1. Detection-as-Code

**Short resume bullet**

Built a CI-tested detection pipeline that blocks security rules from merging unless they catch malicious test events, ignore benign events, and include a written detection strategy.

**Expanded**

Built a detection-as-code workflow for Sigma rules with positive tests, benign false-positive tests, written detection strategy documents, CI merge gates, and automated Elastic query conversion.

**Skills shown**

Detection engineering, Python, CI/CD, Sigma, testing, documentation.

## 2. Prompt-Injection-Hardened LLM Triage

**Short resume bullet**

Built and red-teamed a local AI alert-triage assistant with structured outputs, provenance logging, and a 16-case prompt-injection test harness that documents both blocked attacks and remaining bypasses.

**Expanded**

Built a local Ollama-based SOC triage assistant with input sanitization, strict JSON output validation, provenance logging, and an adversarial test harness. Documented 12 blocked injection cases and four remaining bypass classes instead of claiming complete protection.

**Skills shown**

Applied AI security, Python, adversarial testing, schema validation, SOC workflow design.

## 3. Crown Jewel Triage

**Short resume bullet**

Designed an asset-centered alert prioritization model that ranks security events by business impact and routes them to tier-specific response playbooks.

**Expanded**

Built a six-tier asset criticality model, alert scoring engine, synthetic asset inventory, tier-based response playbooks, and Grafana dashboard definitions to prioritize incidents by what the attacker threatens rather than SIEM severity alone.

**Skills shown**

SOC strategy, risk prioritization, Python, playbook design, metrics, business context.

## 4. Identity-First AWS Incident Response Lab

**Short resume bullet**

Built a Terraform-deployed AWS security lab with identity-focused attack scenarios and custom detections that demonstrate where native cloud monitoring needs additional coverage.

**Expanded**

Built a disposable AWS incident-response lab with intentional identity weaknesses, five controlled attack scenarios, GuardDuty comparison testing, and custom Athena, Elastic, and Panther detections. Added teardown and resource checks to keep the lab repeatable and low cost.

**Skills shown**

AWS security, Terraform, IAM, CloudTrail, GuardDuty, detection engineering, incident response.

## 5. AI Agent Skills

**Short resume bullet**

Built a reusable library of agent skills that turns repeated work into scoped, testable instruction modules with clear triggers, boundaries, and output contracts.

**Expanded**

Published a cross-agent skill library for writing, documentation, UI review, repo onboarding, diagrams, OCR, prompt optimization, file organization, Obsidian workflows, and companion-agent context management.

**Skills shown**

Agent design, prompt architecture, technical writing, workflow automation, tool governance.

## 6. Obsidian Second Brain

**Short resume bullet**

Built a local-first knowledge system that pairs plain Markdown notes with AI-agent rules, reusable workflows, privacy controls, and companion-agent architecture.

**Expanded**

Published an Obsidian second-brain template with beginner bootstrap scripts, agent charters, reusable workflows, security guidance, ADHD-friendly operating rules, conversation-import tooling, and companion-agent memory patterns.

**Skills shown**

Knowledge systems, agent orchestration, privacy design, documentation, Python/shell workflow design, human-centered AI.

## Interview rule

Do not lead with the tool list.

Use this order:

1. **Problem**
2. **Decision**
3. **What you built**
4. **How you tested it**
5. **What still fails**
6. **What you would do next**

That makes the project sound like engineering instead of a lab exercise.
