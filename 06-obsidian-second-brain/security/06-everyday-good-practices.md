# Everyday Good Practices (Plain English)

Audience: a normal professional who wants to use a vault without becoming a security engineer. No jargon. Short list of habits.

If you want the deep version, read the other files in this folder. If you want the version that keeps you safe on a Tuesday, read this one.

---

## Where your vault lives

Your vault is a folder on your computer. That is it.

- Nothing is in the cloud by default.
- Nothing is on an Obsidian server.
- No one at Obsidian can read your notes.

If you want a copy somewhere else, you have to put it there on purpose (backup drive, encrypted sync service, git repo). Nothing moves on its own.

> [!info] Plain English
> Think of your vault like a Word document folder on your desktop. It is as private as that folder. If the folder is on an unencrypted laptop that gets stolen, so is the vault. If the laptop is encrypted, the vault is encrypted.

---

## What NOT to put in your vault

Even if your laptop is encrypted, these are a bad idea in plain markdown:

- **Passwords, API keys, SSH keys.** Use a password manager (1Password, Bitwarden). Not a note.
- **Social Security numbers, government IDs, passport numbers.** If you need to remember them, store in a password manager vault, not a notes vault.
- **Credit card numbers.** Same answer.
- **Other people's secrets.** Confidences shared with you. Health details about family. Someone else's trauma. Even if you trust yourself, you cannot promise the file never leaks.
- **Classified or regulated data.** Any work data under NDA, HIPAA, GDPR, or similar. Keep that in the system of record your employer provides.

If a note starts feeling heavy, move it to a password manager, a locked PDF on an external drive, or just delete the sensitive details and leave the context.

---

## The one Obsidian setting most people get wrong

**Obsidian Sync is a paid add-on that syncs your vault across devices.** It is end-to-end encrypted. That part is good.

But here is the catch most people miss. If you turn on Obsidian Publish (a different add-on), parts of your vault go on the public web. The default feels like "sync" but it is actually "publish."

**Rules of thumb.**
- If you want cross-device sync, Obsidian Sync is fine. End-to-end encrypted. Fine.
- If you want anyone else to read your notes, Obsidian Publish is the right tool. But set up a separate vault for public notes. Never Publish your private vault.
- If you have never touched these settings, do not turn them on until you have a specific reason.

Open **Settings → Core plugins**. Scan the list. If anything named "Sync" or "Publish" is on and you did not turn it on, turn it off and check what you have been publishing.

---

## Backup strategy for normal people

You will lose this vault someday if you do not back it up. Laptops die. Hard drives corrupt. You delete a folder you did not mean to.

Minimum viable backup plan:

1. **Weekly external drive copy.** Buy a cheap USB drive. Once a week, copy your vault folder onto it. Done.
2. **Encrypted cloud copy.** Something like Backblaze, iDrive, or a Cryptomator vault on top of Dropbox. Set it and forget it.
3. **Git repo (optional but great).** `git init` inside your vault. Commit changes once a day. Push to a private GitHub repo. Free. Version history for every note.

Pick two of the three. Three is better. One is better than zero.

**Rule.** The 3-2-1 rule. Three copies, on two different kinds of storage, with one offsite. Internal drive + external USB + cloud = done.

---

## What to do if your laptop is lost or stolen

Short version: if your laptop is encrypted at rest, your vault is safe. If not, assume it is readable by anyone who has the device.

### How to check if your laptop is encrypted

**macOS.** Open **System Settings → Privacy & Security → FileVault**. If it says "FileVault is on," you are good. If not, turn it on today.

**Windows 11.** Open **Settings → Privacy & security → Device encryption** (or **BitLocker** on Pro editions). Confirm it is on.

**Linux.** If you did not pick full-disk encryption at install, you are probably not encrypted. Check with `lsblk` and look for crypt entries, or re-install with LUKS enabled.

### If the laptop is gone

1. Change the password for every service you were logged into on that device.
2. Rotate any API keys that might have been in your terminal history or environment variables.
3. If you have a password manager, trigger a device sign-out from the manager's web dashboard.
4. If you have been pushing your vault to a private git repo, inspect the latest commits for anything you did not mean to commit.

---

## What to do if an AI agent misbehaves

An agent might rewrite a file you did not ask it to touch, or paste something odd into a note. Rare but possible. Steps:

1. **Stop the current session.** Close the terminal or editor window.
2. **Check git history.** If your vault is in git, run `git status` and `git diff`. Roll back with `git checkout -- <file>` on anything the agent changed that you did not want.
3. **Clear the agent's memory.** Each tool has a different way. Claude Code: `/clear` in session, or close the session. Cursor: new chat. ChatGPT: start a new conversation.
4. **Revoke the API key** if you suspect the key was leaked (e.g., the agent printed it to the terminal). Create a new key from the vendor's dashboard.
5. **Review audit logs.** If the vendor offers them (Anthropic, OpenAI both do for paid accounts), check what prompts and responses were logged.
6. **Tighten your charter.** Add a new rule to `CLAUDE.md` that would have prevented the misbehavior. The charter is a living document.

---

## The monthly vault audit habit

Once a month, run this five-minute audit from the vault root.

### On macOS or Linux

```bash
# Possible SSNs (XXX-XX-XXXX pattern)
grep -rE '\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b' . --include='*.md'

# Possible US phone numbers
grep -rE '\b\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}\b' . --include='*.md'

# Possible credit card patterns (16 digits with spaces or dashes)
grep -rE '\b[0-9]{4}[-. ]?[0-9]{4}[-. ]?[0-9]{4}[-. ]?[0-9]{4}\b' . --include='*.md'

# API keys with common prefixes
grep -rE 'sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}' . --include='*.md'
```

### On Windows PowerShell

```powershell
Select-String -Path "*.md" -Recurse -Pattern '\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b'
Select-String -Path "*.md" -Recurse -Pattern '\b\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}\b'
Select-String -Path "*.md" -Recurse -Pattern 'sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}'
```

Any hit is worth checking. False positives are common (a phone number pattern can be an order number). Real positives are the whole point of the habit.

### Or just ask the agent

```
Scan every file in this vault for strings that look like phone numbers, SSNs, credit card numbers, or API keys. List every match with the file path and line number. Do not modify anything.
```

---

## The 60-second summary

- Vault lives on your computer. Not the cloud.
- Do not put passwords, SSNs, or card numbers in markdown. Use a password manager.
- Turn on full-disk encryption today if you have not.
- Back up weekly. Two methods minimum. One of them offsite.
- Audit for leaks once a month. Takes five minutes.
- If an agent goes sideways, roll back with git, clear memory, tighten the charter.

That is the whole file. Come back monthly.

---

<!-- obsidian-second-brain by Emanuel Walker - github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->

_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
