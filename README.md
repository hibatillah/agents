# Skills

Agent skills by [hibatillah](https://github.com/hibatillah)

```bash
# Select skills interactively
npx skills add hibatillah/skills
```

## Available skills

| Skill | What it's for |
|---|---|
| `hibatillah-tone` | Write and rewrite prose in Hibatillah's voice, in English by default or Indonesian on request. Keeps the facts, and adds no motives, results, or promises that were not given. |

## Structure

```text
skills/hibatillah-tone/
├── SKILL.md         scope, language choice, rules shared by both languages
├── en.md            English rules
├── id.md            Indonesian rules
├── examples.md      English patterns, neutral templates, corrections log
├── examples-id.md   Indonesian patterns, neutral templates, corrections log
└── check-voice.py   mechanical checker for both languages
```
