# The Legacy Folder

**The point:** if something happens to you, your family needs a way to reach the important things. The Legacy folder is that way.

This is not morbid. It is the responsible version of adulting. Set it up once, update it twice a year, and your people will thank you if they ever need it.

---

## What goes in `Legacy/`

### Letters
Letters to the people who matter. Written in your actual voice. No performance.
- `Legacy/Letters/to_my_partner.md`
- `Legacy/Letters/to_my_kids.md`
- `Legacy/Letters/to_my_siblings.md`
- `Legacy/Letters/to_my_closest_friends.md`

### Identity
A short record of who you are. Not for the state. For the people reading.
- `Legacy/Identity/who_i_am.md` - the one page summary
- `Legacy/Identity/my_values.md` - the handful of values you actually tried to live by
- `Legacy/Identity/what_i_believed.md` - about God, work, family, death

### Family
Your family tree as you know it. Stories you want preserved.
- `Legacy/Family/family_tree.md`
- `Legacy/Family/stories_from_my_parents.md`

### My Story
The one you would want someone to tell at your funeral if nobody else could.
- `Legacy/MyStory/the_short_version.md`
- `Legacy/MyStory/the_long_version.md`

### Death Stack (practical)
The practical answers your next of kin will need in the first 72 hours.
- `Legacy/DeathStack/password_manager_recovery.md` (how to recover the vault, not the passwords themselves)
- `Legacy/DeathStack/important_document_locations.md` (where the will is, where the deed is)
- `Legacy/DeathStack/accounts_to_close.md` (list of accounts, not the credentials)
- `Legacy/DeathStack/people_to_notify.md` (names and contact methods)
- `Legacy/DeathStack/my_wishes.md` (funeral, burial, service, music)

---

## What stays OUT

- Passwords. Not even your master password. The password manager handles that. Your Legacy folder tells your next of kin which password manager you use and how to initiate the recovery process. Not the password itself.
- API keys. Same reason.
- Anything your family does not need and would not want to find.
- Content that would embarrass someone else if read by your family. If it would hurt them, do not leave it where they will find it.

---

## Encrypt it separately with a shared key

The Legacy folder is important enough to get its own encryption, not shared with your daily vault key. Three options:

### Option 1 - VeraCrypt container with a split passphrase

Create a VeraCrypt container just for `Legacy/`. Pick a strong passphrase. Split it into two parts. Give part one to your most trusted person today. Store part two in a sealed envelope with your will.

Neither party can open the container alone. Both together can.

### Option 2 - Encrypted archive with a shared key via Shamir's Secret Sharing

Tools like [ssss](http://point-at-infinity.org/ssss/) let you split a secret into N shares where any K are enough to reconstruct it. Classic use: 3 of 5 shares reconstruct the key. Give shares to five people you trust. Any three can open the archive. One compromise is not enough.

### Option 3 - Lawyer + sealed instructions

Simplest. Encrypted archive on a USB drive. Decryption key in a sealed envelope. Envelope held by your lawyer or in a safe deposit box with specific access instructions. Low tech, high reliability, works for most people.

---

## Update cadence

- Twice a year, open the folder and reread it.
- After any major life event: new job, new relationship, loss of a loved one, move, kid.
- Keep the letters current. The version from 2019 is not the one your people deserve.

---

## The point once more

Your vault is for you. Your Legacy folder is for the people who outlive you. If you have never written a letter to the people who love you, now is the moment. The system is here. The template is here. Spend 20 minutes.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
