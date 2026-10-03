# Why Severity-Based Triage Is Burning Out Your SOC

Every SOC lead has watched this happen. A Tier 1 analyst closes 180 Mediums in a shift. The 181st was the one that mattered. By the time anybody notices, the attacker has been inside for 11 days and the only question left is how bad the blog post will be.

We blame the analyst. We blame the tooling. We buy a new SIEM. We rotate the on-call. We write a new runbook. Six months later it happens again. On a different team. With a different vendor. In a different industry.

It is not the analyst. It is not the tool. It is the organizing principle.

## The structural problem

Severity labels are assigned by the detection engineer who wrote the rule, usually before they knew which hosts in your environment the rule would fire on. "High" means the detection engineer felt confident the technique is malicious. It does not mean the alert is important.

Severity is a signal about the detection. Not a signal about the asset. Not a signal about the business. Not a signal about what the attacker is actually trying to reach.

When your queue is sorted by severity, you are telling your Tier 1 analyst: "work from the top." The top is whatever the detection engineer felt loud about. That is not a priority queue. That is a confidence queue dressed up as a priority queue.

The result is predictable:

- A Medium on your payment processor sits behind a High on a marketing contractor's laptop.
- An EDR deployment creates 300 benign Highs and the real one on host 301 gets closed as a dupe.
- An analyst who has triaged four hours of PowerShell encoded command alerts starts closing them in 45 seconds without reading the command.
- The P3 queue grows to 4,000 open alerts and becomes an archaeology project nobody is paid to run.

Burnout is the symptom. The queue is the disease.

## What good looks like

Walk into any mature SOC and find the senior analyst who has been there five years. Watch what they do when they pick up an alert. They do not look at the severity first. They look at the host. If the host is the SSO admin console, their eyes narrow and they pick up the phone. If the host is a dev sandbox, they shrug and keep triaging.

They are not reading severity. They are reading the asset.

That senior analyst has an informal tier list in their head. They know the top 20 systems in your company. They know which ones get credentials passed through them. They know which ones are one hop from the crown jewels. They are doing in their head what the queue should be doing in software.

The problem is that she is the only one doing it. She is on PTO this week. The analyst covering for her is on month three. He looks at the severity dropdown because that is what the UI shows him.

Good looks like making the senior analyst's instinct the default behavior of the queue.

## Three-step reframe anyone can start Monday

**1. Name your top 20.**

Pull your top 20 assets by business impact. Not by CMDB count. Not by compliance scope. By what the CFO would call if it went offline for 4 hours. Payment systems. Core customer data stores. SSO and identity providers. CI/CD. Source code. The DNS your customers resolve against. Write them down. 20, not 200. If you cannot fit it on an index card, you have not prioritized, you have inventoried.

Walk this list to your CISO. Ask one question: "If I had to pick 20 things to never let the attacker touch, is this the list?" Expect edits. That is the point.

**2. Tier your top 20 and build a Tier 1 playbook.**

Not a per-alert playbook. One playbook for "ANY alert on any Tier 1 asset." It says: human eyes in 15 minutes, pre-authorized to isolate, communications tree primed, CISO notified by stand-up. Three pages, not thirty.

Then do a Tier 1 fire drill. Pick a random Tier 1 asset. Have someone on your team pretend they just got an alert on it. Walk through the playbook. Time it. Find the gaps. Fix them. Do it again next week with a different asset.

Tier 1 is the one tier you have to get right. The rest you can iterate on.

**3. Rebuild one dashboard panel.**

One. Not the whole SIEM. Just one panel. Call it "MTTR by Asset Tier." Group alert resolution time by tier instead of by severity. Put it on the big screen in the SOC. Watch what happens.

Within a shift, analysts will start noticing which tier they are working. Within a week, they will start asking "what tier is this on?" before they ask "what severity is this?" Within a month, you will have a conversation with your detection engineering team that sounds different.

That conversation is the point.

## The challenge

Severity-based triage is the SOC equivalent of the airline that boards back-of-plane first because that is how it has always been done. It is not evil. It is not stupid. It is a default from an earlier era that nobody has had the time to replace.

You have the time. You just have not spent it yet.

Pick a day next week. Block two hours. Write your top 20. Walk them to your CISO. Pick one, write a one-page tier-based playbook for it, run a drill. Report back.

If you lead a SOC and your queue is still sorted by severity next quarter, your attacker is not the one who should be worried. Your analysts are.
