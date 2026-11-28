---
name: mcp-and-plugin-integration-proof
description: >-
  Use when setting up or testing an MCP server, plugin, connector, or tool
  bridge and you need proof it works end to end.
---
# MCP and plugin integration proof

BLUF: A connection is not an integration. Prove each layer separately, then prove one real result from the real client.

## Steps
1. Write the user action, the components involved, the expected output, and the access boundary. Name the source of truth.
2. Read the provider docs and tool schemas. Note transport, auth method, scopes, and limits.
3. Keep credentials in approved secret storage only. Never put them in tickets, logs, or skill files.
4. Check each layer on its own: service starts, transport handshakes, auth is accepted, client sees the tool list.
5. A handshake with zero visible tools is a milestone, not a working integration.
6. Run one safe read-only tool from the actual client and compare with the documented output.
7. For write flows, get explicit approval, run the smallest allowed write, then read the result back from the real storage.
8. Test denial paths, missing scopes, wrong versions, restarts, and rollback without exposing secrets.
9. Mark each layer PASS, FAIL, BLOCKED, or UNVERIFIED. Say which tests were simulated.
10. Hand off setup and troubleshooting notes with nonsecret repro steps and the next action.

## Done when
- A real client call returned the expected result.
- Any write was read back from storage.
- A saved credential is never reported as a successful login.
