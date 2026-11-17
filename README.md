# Skills

Agent skills by [hibatillah](https://github.com/hibatillah)

## Install

### Claude Code plugin (recommended)

Installs everything in this repo as one plugin, including future commands, subagents, and hooks. Updates come with one command.

```bash
/plugin marketplace add hibatillah/skills
/plugin install hibatillah-skills --marketplace hibatillah/skills

# Update later
/plugin marketplace update hibatillah-skills
/reload-plugins
```

### Generic skills only

For other agents, or to pick individual skills. This installs skills only, not commands or subagents.

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
.claude-plugin/
├── plugin.json        plugin manifest
└── marketplace.json   marketplace listing
skills/hibatillah-tone/
├── SKILL.md         scope, language choice, rules shared by both languages
├── en.md            English rules
├── id.md            Indonesian rules
├── examples.md      English patterns, neutral templates, corrections log
├── examples-id.md   Indonesian patterns, neutral templates, corrections log
└── check-voice.py   mechanical checker for both languages
```
