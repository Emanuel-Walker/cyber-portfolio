# Setup scripts

These scripts create the starter vault structure and choose the correct agent charter.

## macOS or Linux

```bash
bash setup/bootstrap-vault.sh codex
```

Options:

```text
codex
claude
generic
cursor
```

## Windows PowerShell

```powershell
.\setup\bootstrap-vault.ps1 -Agent codex
```

## What the scripts do

- create the standard folders
- copy templates into `99-System/templates/`
- create one root agent charter
- create a local skills index

## What they do not do

- install Obsidian
- install your AI agent
- fill personal placeholders
- import private history
- connect cloud services

Read `../QUICKSTART.md` for the full first-run flow.
