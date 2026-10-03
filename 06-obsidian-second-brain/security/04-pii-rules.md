# PII Rules

**The point:** some things do not belong in a note, encrypted or not. Not because the encryption is weak, but because a note is a bad home for them. Use the right tool.

---

## Never in a vault, even encrypted

| Category | Why not | Right home |
|---|---|---|
| Social Security Number, national ID numbers | Will leak into exports, backups, or screen shares eventually | Password manager with secure note type |
| Bank account numbers, routing numbers, full credit card numbers | Same, plus fraud risk | Password manager or paper in a safe |
| Full passwords | A vault is not a password manager | 1Password, Bitwarden, KeePassXC |
| API keys, access tokens, private keys | Will end up in a commit if you sync | Password manager or a dedicated secrets file outside the vault |
| Medical record numbers, insurance IDs | Regulated and sensitive | A dedicated encrypted file outside the vault |
| Other people's PII without their consent | Ethical and in some jurisdictions legal issue | Do not store it |

---

## OK in a vault, with care

- Your own name, address, phone number. Keep them in one person-of-record file and link to it rather than scattering.
- Dates. Birthdays, anniversaries, work events.
- Observations about people in your life, as long as those observations stay yours and you understand that if your vault leaks, those notes become readable.
- Health notes about yourself in general terms. Not record numbers. Not insurance IDs.

---

## The `#private` tag convention

Any note that contains personal reflection, health observations, or sensitive-adjacent material gets:

```yaml
---
tags:
  - private
---
```

And if you plan to sync via git, include `private` in the filename so `.gitignore` can exclude it. Git cannot read tags, so filename is the belt-and-suspenders convention:

```
04-Areas/Health/private_mood_tracker.md
```

The `.gitignore` in this template already excludes `*private*` from git. Confirm by running `git status` after creating the file and verifying it does not appear.

---

## When in doubt, three questions

1. If this vault leaked tomorrow, which specific note would ruin a week of my life?
2. Of those notes, which contain data a password manager would hold just as well?
3. For the rest, am I comfortable with the encryption and sync setup I have in place?

Answer honestly. Move anything that fails to the password manager. Keep what remains.

---

## The agent and PII

Your agent reads your vault. If you include third-party PII, the agent sees it too. For most offline-first setups this is low risk. For hosted agent setups (where the model is running on a remote server), it is a real consideration. Default assumption: anything in the vault may be read by whatever agent you point at it. Act accordingly.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
