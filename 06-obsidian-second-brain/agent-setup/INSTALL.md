# Agent setup

## Start with the vault bootstrap

From the Second Brain project root:

### macOS or Linux

Codex:

```bash
bash setup/bootstrap-vault.sh codex
```

Claude Code:

```bash
bash setup/bootstrap-vault.sh claude
```

Generic / AGENTS.md-aware tool:

```bash
bash setup/bootstrap-vault.sh generic
```

### Windows PowerShell

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\setup\bootstrap-vault.ps1 -Agent codex
```

Change the agent name as needed.

The script creates the folders, copies templates, and places the correct charter file at the vault root.

## Fill the placeholders

Open the generated charter:

```text
CODEX.md
CLAUDE.md
AGENTS.md
```

Replace every `<ANGLE_BRACKET>` value.

Do not place credentials in the charter.

## Install your agent

Use the agent's current official installation instructions.

This repo intentionally does not pin a third-party CLI install command that may change independently of the vault.

What matters here is the working-directory contract:

```text
launch the agent from the vault root
```

## Validate

Ask:

```text
Summarize the rules in my charter. Do not edit files.
```

Then:

```text
Which folders are protected from unrestricted writes?
```

**PASS:** the answers match the charter.

## Test one controlled write

Ask:

```text
Create a project note under 03-Projects called Agent Setup Test.

Include:
- goal
- status
- next action

Do not modify any other folder.
```

Review the file yourself.

## Add skills later

Vault-local skills live under:

```text
99-System/skills/
```

A reusable public skill library is available in:

```text
../05-ai-agent-skills/
```

when you are using the portfolio copy.

Add skills only after the base charter works.
