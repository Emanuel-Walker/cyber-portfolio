# ADS: Suspicious LSASS Process Access for Credential Dumping

**Rule ID:** 2e8b4d1a-9c7f-4b3e-8a2d-1f5e6c7d8b9a
**Owner:** Emanuel Walker
**Last reviewed:** 2026-09-15
**Status:** experimental

## Goal

Detect a process opening a handle to `lsass.exe` with the specific access rights needed to read its memory. The goal is to catch credential dumping (Mimikatz, ProcDump, comsvcs.dll, direct syscalls) at the moment the handle is requested, before credentials leave the host.

## Categorization

- ATT&CK Technique: T1003.001 (OS Credential Dumping: LSASS Memory)
- ATT&CK Technique: T1003 (OS Credential Dumping)
- Kill Chain Phase: Credential Access
- Priority: Critical

## Strategy Abstract

Windows generates Sysmon Event ID 10 (ProcessAccess) when one process opens a handle to another. For LSASS, the access mask tells us what the caller intends to do. Access masks like `0x1010` (`PROCESS_VM_READ | PROCESS_QUERY_INFORMATION`), `0x1410`, and `0x1fffff` (`PROCESS_ALL_ACCESS`) are consistent with reading LSASS memory. The rule fires on any process-access event targeting `lsass.exe` with one of these masks, unless the source is a known endpoint protection product.

The filter list is maintained by hand. Adding a new tool to the filter requires a code review and an ADS update noting the rationale.

## Technical Context

LSASS holds plaintext credential material in memory while a user is logged in. Attackers read that memory to extract NTLM hashes, Kerberos tickets, and in some configurations cleartext passwords. The read requires opening the lsass.exe process with specific access rights. Sysmon captures this at the handle request, which is earlier than the dump itself.

**Required telemetry:**
- Sysmon Event ID 10 (ProcessAccess) with lsass.exe included in the configuration

**Field mapping (Elastic Common Schema with winlog pass-through):**
- `winlog.event_data.SourceImage`
- `winlog.event_data.TargetImage`
- `winlog.event_data.GrantedAccess`
- `winlog.event_data.SourceProcessId`
- `host.name`

**Reference access masks:**
- `0x1010` = `PROCESS_VM_READ | PROCESS_QUERY_INFORMATION`
- `0x1410` = `PROCESS_VM_READ | PROCESS_QUERY_INFORMATION | PROCESS_DUP_HANDLE`
- `0x1438` = Mimikatz default
- `0x143a` = Mimikatz with ticket operations
- `0x1fffff` = `PROCESS_ALL_ACCESS`

## Blind Spots and Assumptions

- Attackers using direct syscalls to bypass the Windows API can request a handle without touching the standard DLLs. Sysmon still captures the kernel-level access event, so this rule still fires. However, an attacker who duplicates an existing LSASS handle from another process evades the rule because no new access event is generated. Mitigation: alert on anomalous handle duplication separately.
- The rule assumes Sysmon is deployed with a configuration that monitors lsass.exe. Hosts without Sysmon or with a stripped config are invisible.
- Attackers can rename their binary to match a filtered process (`MsMpEng.exe`). The filter is on `SourceImage` path, so a renamed binary not in `C:\ProgramData\Microsoft\Windows Defender\Platform\...` would still alert. Validate this assumption against your EDR's actual install path.

## False Positives

- **Microsoft Defender (`MsMpEng.exe`)** reads LSASS during routine scans. Filtered.
- **Microsoft Defender for Endpoint (`MsSense.exe`)** reads LSASS for behavioral analytics. Filtered.
- **CrowdStrike Falcon (`CSFalconService.exe`)** reads LSASS. Filtered.
- **SentinelOne (`SentinelAgent.exe`)** reads LSASS. Filtered.
- **WSMan provider host (`wsmprovhost.exe`)** reads LSASS during some PowerShell remoting scenarios. Filtered with caution because this process is also abusable. Review quarterly.
- **IR tooling** such as volatility collectors. Not filtered globally. Suppress per-engagement at the SIEM.

## Validation

1. Run the atomic test at `code/tests/atomic_tests/T1003_001_lsass_dump.yml`. The rule must match every event.
2. Run the benign fixture at `code/tests/benign/benign_powershell_admin.yml`. The rule must not match.
3. On a lab host, run `procdump.exe -ma lsass.exe lsass.dmp` as administrator. Confirm an alert within 60 seconds.
4. Run `mimikatz.exe "sekurlsa::logonpasswords"` on an isolated lab host. Confirm the alert fires with a GrantedAccess of `0x1438` or `0x143a`.

## Priority

**Critical.** Successful LSASS access during an active intrusion typically means credentials are in attacker hands within seconds. There is no good reason for an unknown process to read LSASS memory in production. False positive cost is low because the filter list covers the known legitimate readers. Missed detection cost is catastrophic because it enables lateral movement using harvested credentials.
