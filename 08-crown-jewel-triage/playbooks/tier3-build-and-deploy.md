# Tier 3 - Build and Deploy Playbook

**BLUF.** The attacker here does not touch prod directly. They push and prod touches them. The playbook is supply chain. Compare artifacts to known-good. Freeze the pipeline. Rotate build secrets.

**SLA.** MTTD 30 minutes. MTTR 4 hours. Faster if the pipeline runs for a Tier 1 service.

---

## Assets this applies to

- CI/CD orchestrators (Jenkins, GitHub Actions self-hosted runners, GitLab Runner, CircleCI self-hosted, TeamCity)
- Package registries (Artifactory, Nexus, private PyPI, private npm)
- Container image registries (ECR, GCR, Harbor)
- Artifact signing systems (Sigstore, Notary, in-toto, HSMs used for release signing)
- Build secret stores (Vault paths used by CI, GitHub Actions secrets, environment-scoped service accounts)
- IaC repos and the agents that apply them (Terraform Cloud agents, Atlantis, Spacelift workers)

---

## Alerts this covers

- Unsigned or unexpectedly-signed build artifact
- New commit on main from an unexpected author
- Pipeline executed with modified build script
- Service account used from new source IP
- New webhook, new deploy key, new OAuth app on the repo
- Container image pushed outside the pipeline (manual push)
- Package published with hash mismatch
- Build runner process executing unexpected commands (crypto miner, outbound shell)
- IaC apply from unexpected principal

---

## First 15 minutes

1. **Minute 0 to 5.** Freeze the pipeline. Stop accepting new builds. In most CI tools this is a one-click "disable" on the project or org level. Yes, this breaks deploys for everyone on that pipeline. That is the point.
2. **Minute 5 to 10.** Pull the last 10 build runs for the affected pipeline. Compare the build scripts byte-for-byte to the version in the main branch commit history. Mismatches are the lead.
3. **Minute 10 to 15.** Pull the artifact(s) produced by any suspect build. Compare hashes to the last known-good release. If the artifact has already been promoted or pulled by production, you have a bigger problem. Escalate to Tier 1 behavior for the downstream service.

---

## Investigation steps

**Hour 0 to 2:**
- Who had commit access to the pipeline config in the last 30 days? What did they change?
- Who had access to the build runner's host or container? Any new SSH keys, kubeconfigs, agent tokens?
- Pull the build runner's process execution log. Any outbound traffic to non-standard destinations?
- For every artifact built in the suspect window, where was it promoted to? What services pulled it?
- For every secret the pipeline had access to, assume it is burned. Enumerate them. Prepare rotation plan.

**Hour 2 to 4:**
- Determine downstream exposure. If a poisoned artifact was deployed, which production hosts are running it?
- Pull SBOMs for every image built in the suspect window. Diff against the last known-good SBOM.
- If an IaC apply was unauthorized, diff the current cloud state against the last known-good Terraform plan.

---

## Containment options

1. **Pipeline freeze.** Stop new builds. Do not resume until forensics complete.
2. **Credential rotation.** Rotate every secret the pipeline could reach. This includes cloud deploy roles, package registry tokens, signing keys if the runner had access.
3. **Artifact quarantine.** Mark every artifact built in the suspect window as untrusted. Prevent promotion. Prevent pull.
4. **Rollback.** Revert production to the last known-good artifact and configuration. Business decision but SOC advises.
5. **Signing-key ceremony.** If signing keys may be exposed, this is a multi-day event. Plan accordingly. Legal and comms get involved.

---

## Communication tree

- **Immediate:** platform engineering lead, SOC on-call, security engineering (to pull signed artifacts for comparison).
- **Within 1 hour:** CISO, VP Engineering, product owners of affected pipelines.
- **Within 4 hours (artifact confirmed poisoned):** Legal, CTO.
- **Within 24 hours (artifact deployed to customers):** customer success leadership, legal, comms, privacy counsel.

---

## After-action requirements

- Did we have artifact signing in place? If no, that is a Tier 3 ticket out of this incident.
- Did we have provenance (SLSA, in-toto, build attestations)? If no, Tier 3 ticket.
- Were the build secrets scoped tightly, or did one leak give the attacker everything?
- Pipeline freeze latency: how long from alert to freeze?
- Report to CISO within 72 hours.
