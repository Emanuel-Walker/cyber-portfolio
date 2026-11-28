---
name: startup-product-playbook
description: >-
  Use when helping a startup with product decisions, founder-voice writing,
  anti-slop UX/UI, secure builds, or launch, while keeping the founder's intent
  and never inventing proof.
---
# Startup product playbook

This is a standalone Markdown skill. Give it to any coding or general-purpose agent that can read Markdown. It uses no agent-specific commands, plugins, paths, model features, or paid services. Tools are optional. Substitute the equivalent available on the host. The user's instructions and the repository's own rules take precedence.

## When to use it

Use this playbook when the user wants help across several parts of one startup: validating an idea, improving positioning or writing, designing an interface, building software, reviewing security, preparing a launch, or deploying. For a narrow task, use only the relevant parts and complete that task. Do not expand a copy edit into a product overhaul or treat a request for advice as permission to publish.

## Working contract

1. **Start from evidence.** Distinguish repository facts, user-provided facts, external sources, assumptions, and recommendations. Date facts that can change, such as prices, competitors, product features, and regulations.
2. **Preserve intent.** Keep established product behavior, factual copy, brand identity, and deployment configuration unless the user requests a change. For a redesign, keep the product's actual content and functions while developing a new visual direction.
3. **Make one decision at a time.** Identify the current bottleneck and the smallest useful deliverable. Avoid large plans that do not change the next action.
4. **Use real customer evidence.** Simulated boards, personas, and buyer panels can generate hypotheses. They cannot prove demand, willingness to pay, usability, or market size. Label simulations clearly.
5. **Protect claims and data.** Do not invent customers, testimonials, metrics, quotes, credentials, or results. Keep secrets out of source, logs, screenshots, and reports.
6. **Verify outcomes.** A file existing, a test passing, a page rendering, and a deployment serving users are separate observations. Report which ones were actually checked.

## 1. Understand the startup and the repository

When a repository is supplied, inspect its instructions, README, package or build manifests, product documents, current UI, tests, CI, security configuration, and deployment files. Check version-control status before edits. If a connected live product exists, inspect the relevant user journey.

Create a brief working picture in the conversation or a project document when useful:

| Question | What to record |
| --- | --- |
| Customer and buyer | Who uses it, who pays, and what each wants |
| Core job | The task users need to complete and what they do today |
| Product truth | What the code and current release actually do |
| Stage | Idea, prototype, beta, paying customers, or scaling |
| Evidence | Interviews, usage, retention, sales, support, tests, or none yet |
| Constraints | Team, time, budget, platform, brand, accessibility, legal or security needs |
| Release path | Hosting provider, environments, CI, migrations, secrets, and rollback method |

Ask for missing information only when different answers would materially change the work. Continue independent inspection while waiting. Never infer an absent metric or customer quote from a marketing page.

## 2. Product and business decisions

For a new idea or feature, write one testable hypothesis: **a specific customer will perform a specific behavior because the product solves a specific problem**. Name the riskiest assumption, the evidence already available, and the cheapest real-world test that could disprove it. Favor observed behavior over stated enthusiasm.

For a feature choice, compare expected user value, confidence, effort, and dependencies. Define what is in the first release and what evidence would justify the next feature. For pricing or financial questions, show inputs, arithmetic, ranges, and uncertainty. Do not present a model's estimate as a verified market fact.

Useful outputs include a one-page product brief, a prioritized experiment, an MVP scope, a customer interview guide, or a dated competitor comparison. Choose the one that helps the next decision. Do not produce all of them by default.

## 3. Human writing and marketing

### Writing that sounds like the founder

Establish the reader, purpose, relationship, channel, and desired voice. A sample of the founder's own writing is the strongest style reference. Start with the facts and the point the reader needs. Give each paragraph one job. Use concrete wording, natural sentence rhythm, and the level of formality the situation calls for.

When editing, preserve meaning, names, numbers, qualifications, and intentional voice. Remove filler, repeated claims, inflated significance, generic transitions, decorative lists, and stock AI phrasing only where they weaken the text. Do not add artificial typos, anecdotes, emotion, or slang to imitate a human. An AI detector score is not proof of authorship or quality.

### Customer-facing copy

Before drafting, establish the audience, the problem in the customer's language, the offer, the primary action, objections, and available proof. Diagnose whether the task is a blank brief, a rough draft with a real voice, or a small point edit. Change only as much as the task needs.

For each important claim, record its support or mark it as a hypothesis. The homepage headline, call to action, onboarding text, product email, pitch, and documentation should describe the same product. Review copy in the actual interface at mobile and desktop widths. A shorter sentence that wraps badly or hides the next step is not an improvement.

For startup marketing, choose the current bottleneck: customer research, positioning, offer, pricing, acquisition, activation, retention, or launch. Build one coherent plan with an owner, channel, measure, and review date. Publishing, outreach, ads, and spending require authorization for the actual destination and action.

## 4. UX/UI that belongs to the product

### Direction before styling

Identify the user's task, the content they must scan first, the product's subject matter, existing brand, platforms, and target viewports. Select one visual concept that arises from those facts. Write a compact direction for typography, color, spacing, composition, imagery, and motion. Explain how each important choice supports clarity, hierarchy, identity, or use.

Do not use a preset aesthetic because it is fashionable or ban a technique merely because it appears often. Gradients, cards, glass, serif fonts, dark mode, and animation can be appropriate when they serve the product. Reject the automatic combination of generic hero copy, decorative gradient, identical feature cards, stock icons, and motion on every section.

### Match the surface

| Surface | Design priority |
| --- | --- |
| Marketing or landing page | Explain the offer, show the real product, earn trust, and make the next action clear. Use a distinct narrative based on real content. |
| Dashboard or application | Optimize repeated tasks, scanability, navigation, state changes, and error recovery. Put personality in precise details. |
| Documentation or article | Support reading, wayfinding, examples, and comprehension. |
| Portfolio or showcase | Let the work lead. Keep the interface subordinate. |

Design the states users will encounter: loading, empty, partial, error, success, and permission boundaries. Record the trigger, visible feedback, and next safe action for each applicable state. Keep labels consistent across buttons, confirmations, and errors. Verify keyboard operation, visible focus, touch targets, contrast, zoom, reduced motion, and responsive layout where relevant.

### Rendered critique loop

Inspect the actual result at the viewports it will ship at. Look for unclear hierarchy, awkward line breaks, clipped controls, empty visual areas, inconsistent spacing, poor contrast, broken focus, misleading copy, and generic decoration. Ask: **would this layout and visual language still look plausible if the logo and product name were replaced by an unrelated company?** If yes, revisit the product-specific direction. Fix observed issues and inspect the changed result. Do not declare a design complete from code alone.

## 5. Implementation and quality

Follow the repository's language, framework, architecture, and conventions. Keep changes focused and reviewable. Update the UI, API, data model, tests, and documentation together when a feature crosses those boundaries. Prefer existing components and tokens when they fit. Add a new abstraction only when it simplifies repeated work.

Run the checks relevant to the change: build, type checking, meaningful tests, linting, and an end-to-end user path when one is affected. Inspect failures rather than treating a green command as proof that every behavior works. Verify the user path manually or in a browser when visual or interaction quality matters.

## 6. Security and privacy

Security is part of design and implementation, with a deeper review before release. Inspect the trust boundaries that actually exist in the product: browser to API, unauthenticated to authenticated user, user to user or tenant, app to database, third-party webhook, file upload, background job, and agent or model output to tools.

For each boundary, identify the actor, protected resource, permitted action, validation point, and failure mode. Pay particular attention to:

- Authentication, authorization, tenant isolation, and object-level access checks.
- Input validation, output encoding, injection risks, file uploads, and redirects.
- Secret handling, environment variables, logs, client bundles, and repository history.
- Dependency and build provenance, CI permissions, and deployment credentials.
- Data retention, backups, deletion, privacy expectations, and least-privilege access.
- Payments, webhooks, retries, idempotency, and replay protection where present.
- For AI features: prompt injection, untrusted retrieved content, tool permissions, destination validation, cross-user data leakage, and bounded side effects.

Use framework-specific current guidance for the project's actual stack. Confirm a finding with a concrete affected actor, resource, and outcome. Give the source location, safe reproduction or validation status, impact, and smallest effective fix. Distinguish **confirmed**, **likely**, and **needs runtime validation**. Do not run intrusive tests against production or claim a checklist is a security certification.

## 7. Deployment and launch

Inspect the existing hosting provider and release process before choosing a new one. Check environment variables without printing their values, migrations, backups, health checks, domains, CI gates, monitoring, and rollback. Build and test the release candidate, then deploy through the repository's established path or a provider the user has chosen.

After deployment, verify the actual environment: the URL responds, the critical user path works, assets load, errors are visible to operators, and the deployed version matches the intended commit. Report the URL, version, status, checks performed, and any checks that could not be run. A deployment job starting is not the same as a ready release.

When launch communications are in scope, align the announcement, website, onboarding, support material, analytics, and actual product behavior. Do not publish messages, contact customers, change budgets, or deploy merely because a plan mentions those actions. Act when the user has authorized that step.

## 8. Learn from the release

Choose a small set of measures tied to the original hypothesis, such as activation, task completion, repeat use, paid conversion, support volume, or error rate. Record a baseline and review date when data exists. Interpret changes cautiously: usage counts, simulated feedback, and a single customer comment answer different questions. Recommend the next experiment from observed results.

## Delivery format

For substantive work, finish with:

1. **What changed** and why it serves the startup's current goal.
2. **Evidence checked**, separated into repository inspection, tests, rendered UI, live deployment, and customer or market evidence.
3. **Remaining risks or decisions** that materially affect the next step.
4. **Where to find the work**, using file paths, commit or pull request links, and deployment URL as applicable.

For a small request, use a short answer instead of this full structure.

## Provenance

This playbook is an original synthesis of two local combined workflows, `anti-slop-ui-design` and `startup-companion`, and ideas from these public skill projects: [Anthropic frontend-design](https://github.com/anthropics/skills), [Taste Skill](https://github.com/Leonxlnx/taste-skill), [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [Impeccable](https://github.com/pbakaus/impeccable), [Anti Slop](https://github.com/miqdadbadjuber/anti-slop), [Humanizer](https://github.com/blader/humanizer), [Marketing Skills](https://github.com/coreyhaines31/marketingskills), and [Founder Skill](https://github.com/Jakeschincariol/founder-skill). It stands alone. Using those projects is optional. Their original files and licenses remain with their respective authors.
