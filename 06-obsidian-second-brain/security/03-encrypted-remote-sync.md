# Encrypted Remote Sync

**The point:** you want your vault on your laptop and your phone (or two laptops). You do not want a cloud provider reading your notes. Three ways to do it.

---

## Option A - Obsidian Sync (official, paid)

Obsidian's own sync service. End-to-end encrypted with a passphrase only you know. Your notes transit their servers encrypted. They cannot read them.

Pros: zero config, works on mobile, automatic conflict resolution.
Cons: paid, you trust the Obsidian team's implementation.

Fair pick for someone who wants it to just work.

---

## Option B - Git + git-crypt (free, DIY)

A git remote (GitHub, GitLab, Codeberg, self-hosted Gitea) with `git-crypt` transparently encrypting sensitive files before they are pushed.

Pros: free, portable, versioned history, encrypted in transit and at rest on the remote.
Cons: no mobile support out of the box, you handle conflict resolution yourself.

Setup:
```bash
# Install git-crypt
# macOS: brew install git-crypt
# Linux: apt install git-crypt
# Windows: download from https://github.com/AGWA/git-crypt/releases

cd my-vault
git init
git-crypt init

# Decide which files to encrypt. Create .gitattributes:
cat > .gitattributes << 'EOF'
01-Daily-Notes/** filter=git-crypt diff=git-crypt
02-People/** filter=git-crypt diff=git-crypt
04-Areas/** filter=git-crypt diff=git-crypt
09-Dreams/** filter=git-crypt diff=git-crypt
Legacy/** filter=git-crypt diff=git-crypt
EOF

# Export a symmetric key so you can set up a second machine
git-crypt export-key ~/vault.key

# Commit and push
git add .
git commit -m "init vault"
git remote add origin git@github.com:you/private-vault.git
git push -u origin main
```

On a second machine:
```bash
git clone git@github.com:you/private-vault.git
cd private-vault
git-crypt unlock ~/vault.key
```

---

## Option C - Syncthing with encrypted folder

[Syncthing](https://syncthing.net/) is a peer-to-peer file sync tool. Devices sync directly over the network. No cloud involved. Syncthing supports "encrypted folders" so a device acting as a relay never sees plaintext.

Pros: free, no cloud, no account, works on Android, works on Linux servers.
Cons: devices need to be online at the same time to sync (or you keep a Raspberry Pi running), setup is less friendly than Obsidian Sync.

Setup:
1. Install Syncthing on both machines.
2. Add the vault folder on machine A. Share with machine B's device ID.
3. On machine B, accept the share.
4. Done.

---

## Which one?

| Need | Pick |
|---|---|
| It just works, including mobile, do not want to think about it | Obsidian Sync |
| Free, versioned history, do not need mobile | Git + git-crypt |
| Free, want mobile, willing to run Syncthing | Syncthing |

I use git + git-crypt because version history matters more to me than mobile editing. Your tradeoff may differ.

---

## What never gets synced

- Full-disk encryption keys, recovery codes, or API tokens. Even encrypted, these do not belong in a vault.
- The `Legacy/` folder, by default. That one gets its own separate backup. See `05-legacy-folder.md`.
- Anything with `private` in the filename, per the `.gitignore` convention.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
