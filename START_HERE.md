# Start here

You do not need to understand every tool in this repo.

Pick one project. Run its quickstart. See the result. Then read the deeper writeup.

## If you are a recruiter or hiring manager

Start here:

1. **Crown Jewel Triage** if you want to see how I frame security problems.
2. **Detection-as-Code** if you want to see engineering discipline.
3. **AWS Incident Response Lab** if you want cloud security.
4. **LLM Triage** if you want applied AI security.
5. **AI Agent Skills** if you want reusable agent workflows.
6. **Obsidian Second Brain** if you want the human side of AI systems.

Resume-ready summaries live in:

```text
RESUME_PROJECTS.md
```

## If you want to run something

Clone the repo:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio
```

Then pick a project:

| Project | Plain English | Start here |
|---|---|---|
| 01 Detection-as-Code | Test security rules before they reach production | `01-detection-as-code/QUICKSTART.md` |
| 02 LLM Triage | See whether attacker-controlled text can trick a SOC AI assistant | `02-llm-triage-hardened/QUICKSTART.md` |
| 03 Crown Jewel Triage | Rank alerts by what they threaten, not just severity | `03-crown-jewel-triage/QUICKSTART.md` |
| 04 AWS IR Lab | Build a small cloud lab and test identity-focused detections | `04-identity-cloud-ir/QUICKSTART.md` |
| 05 Agent Skills | Install one reusable instruction module into an AI coding agent | `05-ai-agent-skills/QUICKSTART.md` |
| 06 Second Brain | Build a local notes system with an AI thought partner | `06-obsidian-second-brain/QUICKSTART.md` |

## The rule for every project

Each project should answer five questions:

1. What problem does this solve?
2. What did I build?
3. What can I run right now?
4. What should I see when it works?
5. What does this **not** prove?

If a project does not answer all five, open an issue.

## Safety

- Cloud labs belong in accounts you own.
- Attack simulations belong in labs you control.
- Data in this repo is synthetic.
- AI outputs still need human review.
- Local notes do not automatically mean local AI processing.

## First recommendation

If you only run one project today:

```bash
cd 03-crown-jewel-triage
python3 code/crown_jewel_scorer.py \
  --inventory code/example_asset_inventory.yaml \
  --alert code/example_alerts.jsonl
```

It is fast, local, and shows the portfolio's core idea: context changes what matters.
