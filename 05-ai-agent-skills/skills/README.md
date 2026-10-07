# Skills

Each subfolder is one reusable agent skill.

A skill folder should contain:

```text
SKILL.md
```

## A good skill answers

1. When should the agent use this?
2. When should it not use this?
3. What exact steps should it follow?
4. What may it change?
5. What should the output look like?
6. What should it check before handoff?

## Start small

Do not install all skills just because they exist.

Use:

```bash
bash scripts/install-skill.sh claude builder-pack
```

or install one named skill.

## Rule

A skill is not "better" because it is longer.

Prefer:
- clear trigger
- narrow scope
- observable output
- quality check
