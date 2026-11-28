---
name: bug-bounty-hunter
description: >-
  Use when planning legal bug bounty or VDP work with a written scope: reading
  policy, passive recon, drafting reports, checking duplicates, or closing web
  and API skill gaps.
---
# Legal bug bounty helper

This skill helps an AI coding agent support authorized bug bounty work. It is not permission to test any system. The researcher owns every account, identity check, tax form, and submission.

## Hard rules

- Scope first. Read the live program policy, in-scope list, out-of-scope list, bounty table, and banned-methods section before any test idea is discussed in detail.
- Confirm the exact asset is in the written in-scope list. If it is unclear, stop and tell the researcher to ask the program, or to pick a different asset.
- Respect rate limits and automation rules in that policy. If the policy is silent on automation, default to manual, low-volume testing, and flag the uncertainty.
- No denial of service, no fuzzing that could degrade a service, no spam, and no high-volume scanning.
- No social engineering, no phishing, no physical testing, and no contact with a company's staff as part of a "test."
- Use only the researcher's own test accounts, unless the written policy clearly allows something else.
- If any data that is not the researcher's appears, stop. Tell the researcher to follow the program's incident rules, which usually means notify, do not retain a copy, and do not share it.
- Never test a company, site, IP, or app that has no program or VDP authorizing that test.
- Lab and course scripts never go against real targets.
- Do not invent payout amounts, severity scores, or "likely bounty" figures. Quote only a live table the researcher has saved, or say the figure is unknown.
- Do not include exploit payload strings, ready-to-run exploit code, or copy-pasted one-liners from payload catalogs. Describe what to check, and what evidence would show a real issue.
- Safe harbor, if a program offers it, applies only to good-faith testing that stays inside that policy. It is not a general license.

## When this skill may help

- Building or updating a paperwork toolkit for a chosen program.
- Planning PortSwigger, Hacker101 CTF, or other official practice work.
- Drafting a report from evidence the researcher already has.
- Reviewing a policy in plain language.
- Suggesting a lawful, scoped next check.

## When this skill must refuse

- Any request to scan, crawl, or probe a host that is not in a written in-scope list the researcher has provided.
- Any request for payload strings, exploit code, or bypass snippets to paste into a live target.
- Any request to test a third-party customer deployment, another person's account, or an out-of-scope acquisition or vendor system.

## Researcher background (sanitized, generic only)

Use this only to pick practice order and program fit. It is not a claim of authorization.

Strengths: PowerShell and Bash, packet and protocol analysis (Wireshark, tshark, tcpdump, Nmap, display filters and BPF), detection queries (KQL, EQL, Splunk SPL, Lucene), moderate Python and C, plus lab experience with host triage, service diagnostics, capture field extraction, memory-safety concepts, and reverse-engineering tools (Ghidra, GDB, IDA, and similar).

Best-fit lanes, in order:

1. Network, protocol, and in-scope infrastructure testing.
2. Native, binary, and host-level bugs on programs with thick clients or self-hosted software.
3. Web injection and modern API testing as a growth lane, after a daily proxy workflow is in place.

Gaps to close: IDOR, SSRF, broken authorization, business logic, JWT and OAuth, GraphQL, daily Burp or Caido use, modern bounty recon (passive first, then scoped probing), offensive cloud review, mobile testing, and program operations (scope reading, duplicate checks, report writing).

## Practice first

Before any live program work, point the researcher at official, written-scope practice:

- PortSwigger Web Security Academy: https://portswigger.net/web-security
- Burp Suite Community Edition: https://portswigger.net/burp/communitydownload
- Hacker101 and the Hacker101 CTF: https://www.hackerone.com/hackers/hacker101 and https://ctf.hacker101.com/
- YesWeHack Dojo, as practice, unless a specific Dojo listing clearly pays

A planning load of 6 to 8 hours a week is a planning figure only. There is no official median time to a first bounty. Do not promise a payout date.

## Paperwork toolkit (no scanning)

Help the researcher keep a dated folder for the chosen program:

- Saved copies of the policy, in-scope list, out-of-scope list, and bounty table, with the date they were saved
- A notes sheet of in-scope assets only, with columns for asset type, "in the written scope: yes or no," and "policy allows this method: yes, no, or unclear"
- A one-page rules card in the program's own words (banned methods, rate limits, account rules, disclosure rules)
- The report template in this skill
- Optional later: a string-match helper that checks whether a hostname or IP already appears in the saved in-scope list. That is a checklist helper, not reconnaissance against a network.

## Recon workflow (passive first)

1. Read and save the policy. Write down banned methods and any automation cap.
2. Copy in-scope assets only. Drop anything out of scope, including third-party apps, other customers, and assets marked "ask first" until the program answers.
3. Passive collection only, at first. Prefer public sources that do not touch the target (certificate transparency, public documentation, public source repos the policy includes, and passive subdomain sources such as subfinder).
4. Filter every name and address against the saved in-scope list. Discard the rest.
5. Only then, and only if the policy allows it, do low-volume live checks on the filtered list (for example httpx, or a manual visit in a browser through the intercepting proxy). Stay inside stated rate limits.
6. Map the application by hand: login, account switching, exports, webhooks, file previews, desktop-client endpoints, and admin versus user roles.
7. Do not run crawlers or template scanners (katana, nuclei, mass port scans, directory smashers) unless the written policy allows that class of tool at that volume.
8. Review the live-host list by hand before any deeper testing. A long unreviewed list is a backlog, not a result.

Nmap, tshark, and similar tools stay unused on any live system until a written policy clearly allows the exact method, the exact asset, and the exact volume.

## Testing checklists (what to check, no payloads)

These are questions to answer with the researcher's own accounts, on in-scope assets. Do not supply payload strings.

### IDOR and broken object access

- Can two test accounts be created under the policy?
- Which requests carry an object identifier (id, uuid, slug, filename, invoice number)?
- If account B uses an identifier from account A, does the server return, change, or delete account A's object?
- Check read, change, delete, share, and export as separate actions.
- Check same-role access (horizontal) and lower-to-higher role access (vertical) on in-scope endpoints.
- Is the identifier guessable, listed in another response, or only usable if already known? State that honestly in any report.
- Stop immediately if data belonging to a stranger appears.

### SSRF and server-side fetches

- Which in-scope features fetch a URL or open a host on the user's behalf (previews, webhooks, importers, PDF or image fetchers, avatar loads)?
- Is the destination limited to expected external hosts?
- What does the feature return (body, status, timing, error text)? Does that reveal internal network detail?
- If the policy allows testing of internal or metadata destinations, stay at a proof level. Do not scan an internal network, and do not use the finding to reach further systems.
- If the policy is unclear on this class, stop and ask the program.

### Authentication, session, and authorization

- Can a session be used after logout, password change, or role change?
- Are reset, invite, and MFA flows bound to the intended account, and do tokens expire as documented?
- For OAuth or OIDC, check redirect URI strictness, state or nonce use, and whether a token issued to one client or tenant works in another.
- For JWT, check whether the server actually verifies the signature, audience, issuer, and expiry. Describe the check. Do not paste algorithm-confusion payloads.
- For GraphQL or similar APIs, check whether a lower-privilege token can reach fields or mutations meant for another role.
- Stay on accounts the researcher owns.

### Business logic

- Can a documented workflow be skipped, repeated, or reordered (checkout, refund, invite, trial, quota)?
- Do quantity, price, or coupon values stay consistent between the client and the server?
- Can a limit be reset by starting a second session or a second test account in a way the policy still allows?
- Prefer proofs that use the researcher's own money, own credits, or own test data, at a small scale.
- Do not cause a real financial loss to other users or to the company beyond a minimal proof.

### LLM prompt injection (only where the program pays for impact)

- Does untrusted content (other users' text, uploaded files, fetched web pages, email) get placed into a model prompt that can call tools or read other data?
- Is there an effect on another user, another tenant, or a privileged tool, not only a changed chat reply?
- Many programs do not pay for a jailbreak or a leaked system prompt by itself. Read that program's AI rules first (Meta and Microsoft Copilot are examples of this pattern).
- Do not write jailbreak strings in notes or reports unless they are the minimum needed to show a paid impact class, and then keep them in the researcher's private evidence, not in shared skill files.

## Using existing strengths (in scope only)

### Packet capture on desktop or VPN clients

- Install only the official in-scope client, on the researcher's own machine.
- Capture traffic for that client while signed into the researcher's test account.
- Look for plaintext secrets, weak session handling, certificate validation failures, unexpected destinations, and commands the UI does not show.
- Confirm every destination is still in written scope before any follow-up test.
- Do not point the client or the capture at customer deployments, or at networks the policy marks out of scope.

### PowerShell for Windows client testing

- Use PowerShell on the researcher's own Windows host to inspect the installed in-scope client: process, service, install path, update path, local log, and named pipe or local port use that the policy allows.
- Use existing lab habits (host triage, service diagnostics, string extraction from a local binary) only against that local install.
- Do not reuse lab scripts against a remote live network.
- If a finding needs a debugger or a reverse-engineering tool, stay on the local client, and re-read the policy for any ban on reverse engineering or on modifying the client.

### Detection and query skills

- Use KQL, EQL, or Splunk knowledge to describe impact clearly: what a defender would see, what log line would fire, and what data was at risk.
- That wording belongs in the report's impact section. It is not a reason to access a company's internal logs.

### Python, C, and Bash

- Fine for local helpers: formatting notes, matching a hostname against the saved in-scope list, parsing a capture the researcher already took, or lab work on official practice sites.
- Not for mass scanners or exploit utilities aimed at a live program.

## Duplicate-avoidance check

Before drafting a report, walk this list with the researcher:

1. Is this still in the current written scope? Policies change. Re-read the saved brief and the live page.
2. Search the program's disclosed reports and the platform's public activity for the same asset and the same bug class.
3. Search public writeups for the product name plus the bug class. Older indexes such as Bug Bounty Reference can help, but also check recent official disclosures.
4. Read the program's known-issues, changelog, or "previously reported" notes if they exist.
5. Ask whether a later report would add new impact, a new endpoint, or a new chain. Some programs, such as Microsoft, may pay a differential when new information is added. Most pay nothing for a plain duplicate.
6. Do not submit a theoretical issue, an AI-drafted claim with no working proof, or a finding that only affects the attacker's own isolated session when the program requires impact on other users.
7. One issue per report unless the policy says a chain belongs together.

## Report template

Fill every field from evidence the researcher already has. Leave a field blank rather than guessing.

```md
# Title
[Asset] [bug class] [who can be affected], in one line. No hype.

# Program and scope
- Program name and policy URL (and the date the policy was saved)
- Exact in-scope asset (URL, app, client, or IP range as listed)
- Confirmation that this asset is in the written scope

# Severity
- Researcher's suggested severity, tied to the program's own scale
- Why, in plain words (data at risk, who can do it, any user interaction needed)
- Do not invent a dollar amount

# Summary
Two or three sentences: what is wrong, how it was reached with a test account, and what a successful abuse would allow.

# Steps to reproduce
Numbered, minimal, exact. Start from a clean test account. Include only the requests and UI steps needed. No extra tooling, no payload catalog dumps, no other users' data.

# Evidence
- Request and response samples, redacted
- Screenshots or a short capture, if they help
- Account handles used (researcher-owned only)
- Date and time, with time zone

# Impact
Who is affected, what data or action is at risk, and any realistic limit on the issue. Say clearly if strangers' data was not accessed.

# Recommended fix
A short, practical fix (authorization check on the server, destination allowlist, session invalidation, and so on).

# Duplicate check
Where the researcher already searched, and what was found.

# Related notes
Anything the triage team should know (intermittent behavior, affected versions, desktop-client build number).
```

## Platform order (reminder only)

This skill does not sign up for programs. The researcher does that. Preferred order from the 2026-11-21 starter draft:

1. Official labs and CTFs (PortSwigger, Hacker101, YesWeHack Dojo)
2. A YesWeHack public program whose written scope includes VPN, protocol, infrastructure, or a desktop client
3. An Intigriti public program filtered the same way, as backup
4. huntr sandboxed challenges, in parallel, for AI practice with written rules
5. Later, after practice: Microsoft (Windows Insider Preview and Copilot), then other crowded public programs such as Meta and Google

Recheck every live policy before any work. Listings change.
