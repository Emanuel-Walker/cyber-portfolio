# 10-minute quickstart

## Goal

Create a working local notes vault with one AI-agent charter.

You do **not** need to understand Obsidian plugins, MCP, companion agents, or automation yet.

## Option A: easiest public clone

```bash
git clone https://github.com/Emanuel-Walker/obsidian-second-brain.git my-brain
cd my-brain
```

If you are running this from the portfolio copy instead, enter:

```bash
cd 06-obsidian-second-brain
```

## 1. Bootstrap the vault

### macOS or Linux

Pick your agent:

```bash
bash setup/bootstrap-vault.sh codex
```

or:

```bash
bash setup/bootstrap-vault.sh claude
```

or:

```bash
bash setup/bootstrap-vault.sh generic
```

### Windows PowerShell

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\setup\bootstrap-vault.ps1 -Agent codex
```

Change `codex` to `claude` or `generic` if needed.

**PASS:** the script prints three `PASS` lines and tells you which charter file to edit.

## 2. Fill the charter

Open one of:

```text
CODEX.md
CLAUDE.md
AGENTS.md
```

Replace every:

```text
<ANGLE_BRACKET>
```

Keep each answer short.

Do not put passwords, API keys, bank numbers, or government ID numbers in the charter.

## 3. Open the vault

Install Obsidian.

Choose:

```text
Open folder as vault
```

Pick this repo folder.

You should see:

```text
00-Inbox
01-Daily-Notes
02-People
03-Projects
...
99-System
```

**PASS:** those folders appear in Obsidian.

## 4. Launch your agent

Launch your chosen agent **from this folder**.

Then paste:

```text
Summarize the rules in my charter. Keep it under 10 bullets.
```

**PASS:** the answer matches the file you edited.

Then paste:

```text
Which folders are you not allowed to edit freely?
```

**PASS:** the agent names the protected folders from your charter.

## 5. Create one useful note

Paste:

```text
Create a project note for "Second Brain Setup" under 03-Projects.

Include:
- goal
- current status
- next three actions

Do not touch any other folder.
```

**PASS:** one project note appears under `03-Projects/`.

## V1 complete

You now have:
- local Markdown notes
- a folder structure
- an agent rulebook
- one agent-created project note

Stop here for today if that is enough.

## Next

Choose **one**:

- `ADHD-GUIDE.md` for low-friction daily use
- `COMPANION-ARCHITECTURE.md` if you want a persistent personal agent
- `workflows/` for repeatable jobs
- `security/` before putting sensitive material in the vault
- `MUSE-GADGET-SDK.md` if you want a Raspberry Pi to become a physical Muse tool
