param(
  [ValidateSet("claude","codex","generic","cursor")]
  [string]$Agent = "generic"
)

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$folders = @(
  "00-Inbox",
  "01-Daily-Notes",
  "02-People",
  "03-Projects",
  "04-Areas",
  "05-Resources",
  "06-Archive",
  "07-Attachments",
  "08-AI-History",
  "09-Dreams",
  "10-Study",
  "99-MOC",
  "99-System/templates",
  "99-System/skills",
  "Legacy"
)

foreach ($folder in $folders) {
  New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

if (Test-Path "templates") {
  Copy-Item -Recurse -Force "templates/*" "99-System/templates/"
}

switch ($Agent) {
  "claude" {
    if (-not (Test-Path "CLAUDE.md")) { Copy-Item "agent-setup/CLAUDE.md.template" "CLAUDE.md" }
    $Charter = "CLAUDE.md"
  }
  "codex" {
    if (-not (Test-Path "CODEX.md")) { Copy-Item "agent-setup/CODEX.md.template" "CODEX.md" }
    $Charter = "CODEX.md"
  }
  default {
    if (-not (Test-Path "AGENTS.md")) { Copy-Item "agent-setup/AGENTS.md.template" "AGENTS.md" }
    $Charter = "AGENTS.md"
  }
}

if (-not (Test-Path "99-System/skills/INDEX.md")) {
@"
# Local skills

Put vault-specific agent skills here.

Reusable public skills:
https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/05-ai-agent-skills
"@ | Set-Content "99-System/skills/INDEX.md"
}

Write-Host ""
Write-Host "PASS: vault folders created."
Write-Host "PASS: templates copied to 99-System/templates/."
Write-Host "PASS: agent charter ready at $Charter."
Write-Host ""
Write-Host "NEXT:"
Write-Host "1. Open $Charter."
Write-Host "2. Replace every <ANGLE_BRACKET> placeholder."
Write-Host "3. Open this folder as an Obsidian vault."
