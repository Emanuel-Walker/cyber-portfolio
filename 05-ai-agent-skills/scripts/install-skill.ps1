param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("claude","codex","copilot","cursor")]
  [string]$Agent,

  [Parameter(Mandatory=$true)]
  [string]$Item
)

$Root = Split-Path -Parent $PSScriptRoot

switch ($Agent) {
  "claude"  { $Dest = Join-Path $HOME ".claude/skills" }
  "codex"   { $Dest = Join-Path $HOME ".codex/skills" }
  "copilot" { $Dest = Join-Path $HOME ".copilot/skills" }
  "cursor"  { $Dest = Join-Path (Get-Location) ".cursor/skills" }
}

$packs = @{
  "writing-pack" = @("humanizer","article-writing","brand-voice","docs-readability-audit")
  "builder-pack" = @("repo-onboarding-audit","builder-walkthrough","web-ui-audit","prompt-optimizer")
  "second-brain-pack" = @("obsidian","companion-context","file-organizer","docs-readability-audit")
}

if ($packs.ContainsKey($Item)) {
  $Skills = $packs[$Item]
} else {
  $Skills = @($Item)
}

New-Item -ItemType Directory -Force -Path $Dest | Out-Null

foreach ($Skill in $Skills) {
  $Source = Join-Path $Root "skills/$Skill"
  $Target = Join-Path $Dest $Skill

  if (-not (Test-Path (Join-Path $Source "SKILL.md"))) {
    throw "Skill not found: $Skill"
  }

  if (Test-Path $Target) {
    throw "$Target already exists. Review or remove it before reinstalling."
  }

  Copy-Item -Recurse $Source $Target
  Write-Host "INSTALLED: $Skill -> $Target"
}

Write-Host ""
Write-Host "PASS: install complete."
Write-Host "Start a new agent session before testing skill discovery."
