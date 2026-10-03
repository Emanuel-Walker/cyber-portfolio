# Encrypt Your Vault at Rest

**The point:** full-disk encryption is table stakes. Vault-level encryption is one more layer on top. If someone steals your laptop or your external backup drive, your notes stay unreadable.

---

## Baseline: full-disk encryption

Turn this on today if you have not already.

- **macOS:** FileVault. System Settings > Privacy & Security > FileVault. Turn on. Save the recovery key somewhere other than the laptop.
- **Windows:** BitLocker (Pro, Enterprise, Education editions). Control Panel > System and Security > BitLocker Drive Encryption. Save the recovery key to a USB stick or a password manager.
- **Linux:** LUKS, set up at install time. If you did not do it at install, you can migrate but it is painful. Easier to reinstall.

Full-disk encryption protects you when the laptop is powered off. It does not help if the laptop is unlocked and someone walks away with it. For that, use the vault-level encryption below.

---

## Option A - Encrypted folder with VeraCrypt (cross-platform)

[VeraCrypt](https://www.veracrypt.fr/) creates an encrypted container file that mounts as a virtual drive. Your vault lives inside the container. When unmounted, the vault is a single opaque blob.

Pros: cross-platform. Battle-tested. Free.
Cons: you have to mount and unmount manually. Obsidian plugins that watch the filesystem can get confused during unmount.

Setup:
1. Install VeraCrypt.
2. Create a container file, say `vault.hc`, sized for your vault plus growth (10 GB is generous).
3. Mount it. Pick a drive letter (Windows) or mount point (macOS/Linux).
4. Move your vault into the mounted drive.
5. Point Obsidian at the new location.

---

## Option B - Windows: BitLocker on a folder

Windows does not natively encrypt individual folders with BitLocker, but you can create a VHDX file, enable BitLocker on it, and mount it as a drive. Same shape as VeraCrypt but using the Microsoft toolchain.

```powershell
# Create a 10 GB VHDX
New-VHD -Path "C:\vault.vhdx" -SizeBytes 10GB -Dynamic

# Mount, initialize, format, and enable BitLocker through the GUI
# Disk Management > Attach VHD > Initialize > New Simple Volume > Format NTFS
# Then: Control Panel > BitLocker Drive Encryption > Turn on BitLocker on the new drive
```

---

## Option C - macOS: encrypted sparse bundle

```bash
hdiutil create -size 10g -type SPARSEBUNDLE -fs HFS+J -encryption -volname "Vault" ~/vault.sparsebundle
```

You will be prompted for a password. Double-click the `.sparsebundle` to mount it. Vault goes inside.

---

## Option D - Linux: gocryptfs

[gocryptfs](https://nuetzlich.net/gocryptfs/) encrypts a directory tree, file by file. Reader-friendly if you want to sync encrypted files to a remote without exposing filenames or contents.

```bash
# Install (apt example)
sudo apt install gocryptfs

# Initialize an encrypted directory
mkdir vault_encrypted vault_plain
gocryptfs -init vault_encrypted
gocryptfs vault_encrypted vault_plain

# Point Obsidian at ./vault_plain
# When done: fusermount -u vault_plain
```

---

## Which one should you pick?

- **Cross-platform laptop, no sync concerns:** VeraCrypt.
- **Windows only, want native tooling:** BitLocker on VHDX.
- **macOS only:** sparse bundle.
- **Linux and planning to sync encrypted files to a cloud:** gocryptfs.

All of them do the job. The best one is the one you will actually use. Pick, set up, and move on.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
