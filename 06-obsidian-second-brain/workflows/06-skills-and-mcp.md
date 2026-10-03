# Workflow 06 - Skills and MCP Servers

**When to use it:** once your base vault is working and you want the agent to do more specific jobs well.

**What skills are:** small markdown files that tell your agent "when the user asks for X, follow these steps." Skills turn an agent from a generalist into a toolkit.

**What MCP is:** Model Context Protocol. A standard way to give your agent extra capabilities like web search, filesystem access beyond the vault, GitHub operations, or database queries.

---

## Adding skills to Claude Code

Claude Code loads skill files from `99-System/skills/` (or whatever folder you configure in `CLAUDE.md`). A skill is a markdown file with a name, a trigger, and instructions.

### Example skill: `99-System/skills/weekly-review.md`

```markdown
# Skill: Weekly Review

**Trigger:** user says "run the weekly review" or "wrap the week"

**Steps:**
1. Identify the current week number and date range.
2. Read every file in 01-Daily-Notes/YYYY/MM-MonthName/ for that week.
3. Build a review using templates/weekly-review.md as the shape.
4. Save to 01-Daily-Notes/YYYY/MM-MonthName/YYYY-WK-NN_review.md.
5. Report to the user: files read, output path, one honest observation.

**Voice:** operational.
```

Once the skill file exists and your charter points at the skills folder, the agent will auto-apply the skill when you say the trigger phrase. No need to explain the whole workflow each time.

### Starter kit of skills to consider

- `brain-dump-cleanup` - the Inbox cleanup from workflow 01
- `weekly-review` - the review from workflow 04
- `project-kickoff` - creates a new project folder with the kickoff template
- `person-note-create` - creates a new person note stub when a name appears
- `document-to-md` - runs pandoc or whisper on a dropped file and routes the output

See [Emanuel-Walker/cyber-portfolio/tree/main/05-ai-agent-skills](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/05-ai-agent-skills) for a reference set of agent skills you can adapt. Fork and strip what you do not need.

---

## Adding MCP servers

MCP servers plug into your agent to give it capabilities beyond file read and write. Common useful ones:

| Server | What it adds |
|---|---|
| `filesystem` | Read and write files outside the vault with your permission |
| `github` | Open PRs, read issues, review commits from inside the agent |
| `fetch` or `web-search` | Pull web pages and search results into the agent context |
| `memory` | Persistent memory across sessions |
| `brave-search` | Private web search alternative |

### Installing an MCP server for Claude Code

Edit `~/.config/claude/mcp.json` (or the platform equivalent):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/absolute/path/to/vault"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

Restart the agent. Confirm it loaded the servers by asking: "What MCP tools do you have access to?"

### Pick a short list

A long MCP list slows the agent down and expands your attack surface. Start with:

1. Filesystem (so the agent can read source material outside the vault when you point it there)
2. One web tool (search or fetch, your pick)
3. GitHub if you code

Add more only when a specific job needs them.

---

## Rule of thumb

- A skill is for a workflow you do repeatedly inside the vault.
- An MCP server is for a capability the agent does not have at all.

If you find yourself writing the same prompt three weeks in a row, turn it into a skill. If you keep saying "I wish you could just check GitHub," add the MCP server.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
