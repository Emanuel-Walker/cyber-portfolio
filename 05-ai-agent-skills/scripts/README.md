# Skill installer scripts

These scripts copy skills into common agent skill folders.

## macOS or Linux

```bash
bash scripts/install-skill.sh claude humanizer
bash scripts/install-skill.sh codex builder-pack
```

## Windows PowerShell

```powershell
.\scripts\install-skill.ps1 -Agent codex -Item builder-pack
```

## Safety

The installers stop when the destination folder already exists.

They do not silently overwrite an installed skill.

Review a `SKILL.md` before installing it.
