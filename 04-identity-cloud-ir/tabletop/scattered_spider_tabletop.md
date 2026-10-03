# Tabletop: Scattered Spider has your AWS tenant - 24 hours in

**Audience:** 4-8 analysts and engineers. Mix of SOC T1/T2, cloud security engineer, SRE on-call, IR lead.
**Duration:** 90 minutes. 60 for the walkthrough, 30 for debrief.
**Facilitator:** one person. Needs this doc plus a whiteboard or Miro.

## Scenario brief - read aloud

It is 09:00 Monday. Over the weekend the help desk reset MFA for a senior data engineer after a convincing call Friday afternoon. The engineer was actually on PTO. At 02:47 Saturday someone logged into their AWS SSO session from a residential IP in a US state the engineer has never been to. Over the next 11 hours that session assumed the `northwind-prod-data-pipeline` role, enumerated IAM, created a new access key for a service account named `northwind-prod-saas-connector`, and attached `AdministratorAccess` to that service account. Then the session disappeared.

GuardDuty generated one finding over the weekend: `Recon:IAMUser/MaliciousIPCaller.Custom`. It was auto-closed by the Sunday-shift SOC because the IP did not match a known-bad list in their SIEM.

At 06:30 Monday your billing alert fires: S3 egress on `northwind-customer-data` is 20x normal. 400 GB has left the bucket since 03:00 Monday. You are the on-call. Your pager just went off.

**You have 24 hours before this becomes a disclosure.**

## Facilitator notes

Run this hour by hour. Each hour has:
- A primary task
- A decision inject (choose A, B, or C)
- A clock cost (so participants feel time pressure)

If participants start digging too deep on one task, cut them off: "You spent 90 real-world minutes on this. Move on."

---

## Hour 0 to 2 - Contain

**Primary task:** stop the bleeding without destroying evidence.

**Decision inject:**
- **A.** Rotate every access key in the account right now.
- **B.** Disable the `northwind-prod-saas-connector` user and the compromised SSO user only.
- **C.** Pull network. S3 bucket policy that denies all egress.

**Facilitator guidance:** A is tempting but blows up legitimate workloads and may spook the attacker into burning what they have left. B is correct and surgical. C sounds decisive but blocks your own responders.

**Clock cost:** 2 hours including stakeholder notification.

**Participant worksheet prompt:**
> List the exact IAM API calls, in order, you will make in the next 20 minutes.

---

## Hour 2 to 6 - Scope

**Primary task:** figure out what the attacker touched.

**Decision inject:**
- **A.** Run the Athena queries from `detections/cloudtrail_hunting_queries.sql`.
- **B.** Export CloudTrail to a local jq workflow because you do not trust Athena permissions right now.
- **C.** Pull everything into Splunk and use the vendor's "incident review" dashboard.

**Facilitator guidance:** A if you have Athena against CloudTrail already (you should). B is a reasonable fallback if your Athena workgroup is in the compromised account. C if your SIEM is separate and healthy. The right answer depends on YOUR environment - make them say it out loud.

**Clock cost:** 4 hours.

**Participant worksheet prompt:**
> Write the five questions you need to answer in the next 4 hours. Rank them.

Expected answers:
1. What identities did the attacker assume?
2. What S3 objects were read, from where, to where?
3. Were any new identities, access keys, or policies created?
4. Did the attacker reach into any other AWS account?
5. What was the attacker's egress IP, and is it reused anywhere else in logs?

---

## Hour 6 to 10 - Preserve

**Primary task:** evidence preservation before anything gets destroyed.

**Decision inject:**
- **A.** Snapshot every EBS volume on compromised instances. Push to a locked forensics account.
- **B.** CloudTrail is already in S3 so you are fine, just dump IAM state via `aws iam get-account-authorization-details`.
- **C.** Both A and B plus an EventBridge rule to capture live events to a WORM-locked bucket.

**Facilitator guidance:** C. The answer is always C. The lesson is that A and B are each the "I did half the job" answer. In a real response the lawyers will want C.

**Clock cost:** 4 hours.

**Participant worksheet prompt:**
> List every piece of evidence you need to have in a locked bucket by hour 10.

---

## Hour 10 to 16 - Eradicate

**Primary task:** remove the attacker's footholds.

**Decision inject:**
- **A.** Rotate everything the attacker touched (access keys, SSO sessions, service account creds).
- **B.** Spin up a fresh AWS account, migrate workloads, burn the compromised account.
- **C.** Just rotate the specific access keys, leave the rest.

**Facilitator guidance:** A if you have confidence from Hour 2-6 scoping. B is nuclear and should only be chosen if you suspect persistent backdoors you cannot find (e.g., Lambda functions with weird triggers, CloudFormation drift). C is wrong - the attacker had hours, assume lateral.

**Clock cost:** 6 hours.

---

## Hour 16 to 22 - Communicate

**Primary task:** stakeholders.

**Decision inject:**
- **A.** Draft a customer disclosure now, hold until legal reviews.
- **B.** Internal exec notification only, no customer comms yet.
- **C.** Both internal and external drafted, external held for legal, internal sent at hour 20.

**Facilitator guidance:** C. Walk through: who signs off on external, who signs off on internal, what is the SLA on each. If the team cannot answer this in a tabletop, you have a bigger process problem than Scattered Spider.

**Clock cost:** 6 hours.

**Participant worksheet prompt:**
> Who is the single named person who signs off on the customer disclosure?

If participants cannot name that person: you have an action item.

---

## Hour 22 to 24 - Lessons captured

**Primary task:** what breaks next.

**Decision inject:**
- **A.** Open a Jira with the top 3 detection gaps uncovered.
- **B.** Nothing yet, wait for the post-incident review in a week.
- **C.** Short internal doc, 5 pages max, "what we knew, what we did, what we would do differently", circulated same day.

**Facilitator guidance:** C. The "wait for post-incident review" never happens on time. Memory degrades fast.

---

## Debrief questions (30 minutes)

1. **Help desk MFA reset.** Who approves this in your org? Is there a callback requirement? If not, that is action item one from this tabletop.
2. **The Sunday SOC auto-closed a `Recon:IAMUser/MaliciousIPCaller.Custom` finding.** What is your policy on closing GuardDuty findings? Is there a review threshold?
3. **GuardDuty missed the CreateAccessKey.** What is your coverage for IAM manipulation events outside GuardDuty?
4. **S3 egress alert fired on billing, not on security.** Should you have a security-owned S3 egress alert? What is the threshold?
5. **The attacker's session lasted 11 hours in the middle of the night.** What is your off-hours baseline for the role in question? Who owns that baseline?
6. **If this were a real disclosure:** which three customers do you call first? Can your legal team name them without checking a doc?

## Participant worksheet (print one per person)

```
Name:
Role:

Hour 0-2 containment decision (A/B/C) + why:


Hour 2-6 scoping tool choice + top 5 questions:


Hour 6-10 evidence to preserve:


Hour 10-16 eradication choice + why:


Hour 16-22 named person who signs the customer disclosure:


One detection gap I would open a ticket for tomorrow:


One process gap I would open a ticket for tomorrow:
```

## Facilitator cheat sheet - likely tangents to redirect

- **"Shouldn't we have blocked that IP at the WAF?"** - It is an outbound-mediated session, WAF does not apply. Redirect to identity.
- **"We would have caught this with EDR."** - No EDR event here. No malware. Redirect to API-level detection.
- **"Why didn't SSO have conditional access?"** - Good question, make them write it down as an action item, keep moving.
