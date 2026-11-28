---
name: single-question-security-check
description: >-
  Use when a sign-in, new account, password, or payment alert arrives that the
  agent did not cause and only the user can confirm.
---
# Single-question security check

BLUF: One short message per alert, stating only what the source names, asking one question, then staying quiet on that thread for the day.

## Steps
1. Read the alert in full. A subject line is not enough.
2. State what it names: service, time, kind of change.
3. State what it leaves out when that matters: account, amount, device.
4. If it might link to a known open thread, label that as a guess only.
5. Ask one question: was this you, or was this expected?
6. Give the safe route for a no: open the official app or type the official address yourself, never use a link in the alert.
7. Draft it alone. Send externally only with the owner's explicit approval for that destination and exact text through the host's sending rules. Never stack alerts or bundle them with routine updates.
8. Stay silent on that thread for the rest of the day.
9. When the user answers, record it with the date. If no answer, carry it as unconfirmed without re-asking.

## Done when
- One check drafted, or an explicitly authorized check sent, and the thread marked confirmed, denied, or unconfirmed.
