# Agents

Agent skills and tooling by [hibatillah](https://github.com/hibatillah). Skills and commands are available now; subagents and hooks will follow.

## Install

### Claude Code plugin (recommended)

Installs everything in this repo as one plugin, including future subagents and hooks. Updates come with one command.

```bash
/plugin marketplace add hibatillah/agents
/plugin install hibatillah@hibatillah-agents

# Update later
/plugin marketplace update hibatillah-agents
/reload-plugins
```

### Generic skills only

For other agents, or to pick individual skills. This installs skills only, not commands or subagents.

```bash
# Select skills interactively
npx skills add hibatillah/agents
```

## Available skills

| Skill  | What it's for                                                                                                                                                                  |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `tone` | Write and rewrite prose in Hibatillah's voice, in English by default or Indonesian on request. Keeps the facts, and adds no motives, results, or promises that were not given. |

## Available commands

| Command                      | What it's for                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `/hibatillah:docker-cleanup` | Windows only. Prune Docker build cache, then compact the Docker Desktop (WSL2) VHDX so freed disk space returns to Windows. |

## Structure

```text
.claude-plugin/
├── plugin.json        plugin manifest
└── marketplace.json   marketplace listing
commands/
└── docker-cleanup.md  /hibatillah:docker-cleanup
scripts/
└── docker-reclaim.ps1 VHDX compact helper, called by docker-cleanup
skills/tone/
├── SKILL.md         scope, language choice, rules shared by both languages
├── en.md            English rules
├── id.md            Indonesian rules
├── examples.md      English patterns, neutral templates, corrections log
├── examples-id.md   Indonesian patterns, neutral templates, corrections log
└── check-voice.py   mechanical checker for both languages
```
