# Tier 2 - High-Trust Identity Playbook

**BLUF.** Identity compromise is everyone's keys. The playbook is session kill, token rotation, and mass reauth. Fast.

**SLA.** MTTD 15 minutes. MTTR 2 hours.

---

## Assets this applies to

- SSO / IdP tenants (Okta, Entra ID, Ping, Auth0)
- Cloud org admin consoles (AWS organization root, Azure global admin, GCP org admin)
- Active Directory domain controllers
- Password / secrets vaults (Vault, Secrets Manager at org scope, 1Password Enterprise)
- MFA back-ends and recovery flows
- Privileged Access Management systems (CyberArk, BeyondTrust)

---

## Alerts this covers

- Credential stuffing or password spray against the IdP
- MFA fatigue / push-bombing patterns
- Impossible travel on administrator accounts
- Admin role assignment outside change-window
- New federation trust, new SAML app, new OIDC client registration
- Session token theft indicators (anomalous device ID, cookie reuse from new IP)
- Service principal / app registration with unexpected API grants
- Any alert on the SSO or identity management plane

---

## First 15 minutes

1. **Minute 0 to 3.** Pull the admin audit log for the IdP for the last 60 minutes. What changed, by whom, from where.
2. **Minute 3 to 7.** Identify the suspect principal(s). If an admin role was assigned, who assigned it and who received it. If a new app registration was created, who created it and what scopes.
3. **Minute 7 to 10.** Containment decision. Pre-authorized:
   - Suspend the suspect principal (session kill + account disable)
   - Revoke all active sessions for the suspect principal across every federated app
   - Rotate any OAuth/API tokens tied to the suspect principal
   - Revoke any new app registrations created in the suspect window
4. **Minute 10 to 15.** Declare incident. Page identity engineering lead and CISO. Begin broader session analysis.

---

## Investigation steps

**Hour 0 to 1:**
- Pull every authentication event for the suspect identity for the last 24 hours. Not just successful. Including failures and MFA prompts.
- For every app the suspect identity touched, pull the activity log inside that app for the suspect window.
- Check for OAuth consent grants in the last 7 days. Attackers love persistent app consent for post-containment access.
- Check for recovery flow usage (SSPR, forgot MFA) in the last 7 days.

**Hour 1 to 2:**
- Determine blast radius. If the suspect was an admin, every account they could have touched is in scope.
- Identify downstream containment: do we need to force reauth on every user, or just the suspect's downstream?
- If a new federation trust or SAML app was created, dump its config. These persist across password resets.

---

## Containment options

Ranked by blast radius, smallest first:

1. **Single principal suspend.** Suspect account disabled, sessions killed, tokens rotated. Works if you are confident the compromise is scoped to one identity.
2. **Delegated-admin kill.** Suspend the suspect plus every account the suspect created or modified in the suspect window.
3. **Admin-role mass rotation.** All admin role holders reauth, all admin tokens rotated. Noisy. Appropriate when attacker had admin and dwell time is unknown.
4. **Tenant-wide session reset.** Every user reauths. Nuclear. Appropriate when attacker had org-admin and backup accounts may exist.
5. **Federation break-glass.** Disable federation, revert to local accounts for a defined set, rebuild federation trust from known-good config. Last resort. Expect business pain.

---

## Communication tree

- **Immediate:** identity engineering lead, SOC manager, incident commander.
- **Within 30 min:** CISO.
- **Within 1 hour:** CIO if business ops will be affected.
- **Within 4 hours (confirmed admin compromise):** Legal, every business owner whose app is federated.
- **Within 24 hours (customer-facing identity):** Privacy counsel, customer notification planning.

---

## After-action requirements

- Timeline and SLA conformance.
- Was the attacker's path a known attack pattern (push-bombing, token theft, SSPR abuse)? If so, do we have a tuned detection for it now?
- Which detections fired, which did not? Any missed detection on the identity plane is a tier 2 engineering ticket.
- Did we hit the suspect window with session kill, or did sessions persist? Session-kill latency is a known problem with many IdPs. Measure yours.
- Do we have the OAuth / app registration inventory baseline we need to detect a repeat?
- Report to CISO within 72 hours.
