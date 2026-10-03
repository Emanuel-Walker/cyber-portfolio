# Local-First

**The point:** your notes live on your laptop as plain `.md` files. Nothing leaves your machine unless you decide. No vendor training on your writing. No account to lose. No subscription to maintain. The only thing between you and your notes is a text editor.

---

## Why this matters

Every cloud note app is a bet that the company will stay in business, keep its pricing stable, and not change its terms of service in a way you hate. Three bets, compounded over the ten or twenty years you want this knowledge to last. The expected value of that bet is bad.

Local-first flips the risk. The company that makes Obsidian could disappear tomorrow and your notes would still open in VS Code, in Vim, on your phone with any text editor. The file format is markdown, which is a 20-year-old standard that will outlive us all.

---

## What "local-first" actually means in practice

1. **The source of truth is on your disk.** Not in a cloud database.
2. **Sync is optional and under your control.** If you want your notes on two devices, you pick the sync method. See `03-encrypted-remote-sync.md`.
3. **Backups are your job.** No automatic cloud backup means you need a backup plan. Three options: Time Machine, a nightly `rsync` to an external drive, or an encrypted git remote. Pick one. Set it up today.
4. **Portability is free.** Any file can be opened in any text editor. Any folder can be moved to another computer with a drag.

---

## What you give up

Be honest about the tradeoff.

- No "share this note with a link." You can export, but there is no magic URL.
- No real-time collaboration. If you need that, pair this vault with a separate collaboration tool.
- You own the backup problem. If your laptop dies and you have no backup, your vault is gone.

For most security-minded people and most ADHD builders, these are fair trades.

---

## The security case

If you work in security, you already know the argument. Every third-party service is a potential breach vector. Every cloud note is one SSO misconfiguration away from being readable by someone you did not invite. Local files, encrypted at rest, synced only through channels you control, are a smaller attack surface by a wide margin.

The vault still is not a safe for credentials. See `04-pii-rules.md` for what should never go in a note, encrypted or not.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
