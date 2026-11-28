# Tier 5 - Lateral Stepping Stones Playbook

**BLUF.** The asset itself is not valuable. Its position is. Treat it as a tripwire. Focus is east-west traffic since the last known good login.

**SLA.** MTTD 1 hour. MTTR 8 hours.

---

## Assets this applies to

- SSH jump hosts and bastions
- VPN concentrators (SSL-VPN, IPSec concentrators)
- RDP gateways
- Shared service accounts with cross-asset access
- Terraform / Ansible / Puppet masters that touch many hosts
- Backup servers and backup agents with wide read access
- Monitoring agents with privileged collection scopes

---

## Alerts this covers

- Authentication to the jump host from an unexpected source
- Session count anomaly on the bastion
- VPN session from a geography the user has never used
- Service account used from a new host
- Automation master executing a job outside the known schedule
- Any process execution on the bastion that is not SSH, VPN, or the authentication daemon

---

## First 60 minutes

1. **Minute 0 to 15.** Pull every session established on the stepping stone in the last 24 hours. Who, from where, to where.
2. **Minute 15 to 30.** For every suspect session, identify downstream hops. What assets did they SSH to, RDP to, run a job against.
3. **Minute 30 to 45.** For every downstream hop, is it a higher tier (1, 2, 3)? If yes, escalate the downstream to its own tier's playbook immediately. The stepping stone is secondary.
4. **Minute 45 to 60.** Containment decision for the stepping stone: session kill, credential rotation, isolation.

---

## Investigation steps

**Hour 0 to 4:**
- Full east-west map for the suspect window. Every connection out of the stepping stone, every target.
- Credential inventory on the stepping stone. SSH keys, SSH certs, cached kubeconfigs, cached cloud credentials, agent-forwarded sessions. Assume all compromised.
- Check for persistence: new SSH authorized_keys entries, new scheduled tasks, new systemd units, new PAM modules.
- Pull sudo logs if present.

**Hour 4 to 8:**
- For every downstream asset touched in the suspect window, decide if independent investigation is needed.
- Rotate every credential the stepping stone had access to.
- Rebuild the stepping stone from known-good image if dwell time is unknown.

---

## Containment options

1. **Session kill.** Terminate all active sessions on the stepping stone.
2. **Credential rotation.** Every key, cert, service token the stepping stone could use.
3. **Network isolation.** Prevent new inbound and new outbound from the stepping stone. Snapshot for forensics.
4. **Rebuild from known-good.** Default for Tier 5 if dwell time is unclear. Rebuilding is cheap compared to the downstream risk.

---

## Communication tree

- **Immediate:** infra on-call, SOC on-call.
- **Within 2 hours:** identity engineering if the stepping stone is credential-based (bastion with user keys), SOC manager.
- **Within 4 hours:** CISO if any Tier 1 or Tier 2 asset was downstream of a suspect session.

---

## After-action requirements

- Was the stepping stone's credential scope appropriate? Most are over-privileged.
- Did we have session recording on the stepping stone? If no, Tier 5 ticket.
- Did we have anomaly detection on session count and session destination? If no, Tier 5 ticket.
- Rebuild cadence: how often is this stepping stone rebuilt from image? If answer is "never," that is a problem.
- SLA conformance.
