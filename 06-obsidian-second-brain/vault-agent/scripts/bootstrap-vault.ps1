param(
  [ValidateSet("claude","codex","generic","cursor")]
  [string]$Agent = "generic"
)

$Root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
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
  "99-System/companion",
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
    if (-not (Test-Path "CLAUDE.md")) {
      Copy-Item "vault-agent/templates/CLAUDE.md.template" "CLAUDE.md"
    }
    $Charter = "CLAUDE.md"
  }
  default {
    if (-not (Test-Path "AGENTS.md")) {
      Copy-Item "vault-agent/templates/AGENTS.md.template" "AGENTS.md"
    }
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

$companionFiles = @(
  "ABOUT-ME.md",
  "CURRENT-SEASON.md",
  "PROJECTS.md",
  "COMPANION-RULES.md"
)

foreach ($file in $companionFiles) {
  $path = Join-Path "99-System/companion" $file
  if (-not (Test-Path $path)) {
    $name = $file.Replace(".md","")
    "# $name`n`n[FILL THIS IN]" | Set-Content $path
  }
}

Write-Host ""
Write-Host "PASS: vault folders created."
Write-Host "PASS: templates copied to 99-System/templates/."
Write-Host "PASS: companion context folder created."
Write-Host "PASS: Vault Agent charter ready at $Charter."
Write-Host ""
Write-Host "NEXT:"
Write-Host "1. Open $Charter."
Write-Host "2. Fill any placeholders you want to customize."
Write-Host "3. Open start-here/README.md and continue at the Vault Agent validation step."
