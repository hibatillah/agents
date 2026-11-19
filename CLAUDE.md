# CLAUDE.md

Guidance for agents working in this repo (`hibatillah/agents`). It holds his agent tooling, packaged as one Claude Code plugin (`.claude-plugin/`). Today it holds skills, the first being `skills/tone`, invoked as `/hibatillah:tone`. Commands, subagents, and hooks will be added later.

## Layout

- Put each component type in its plugin-standard directory at the repo root: `skills/`, `commands/`, `agents/`, `hooks/`.
- Put helper files a command or hook runs in `scripts/`, and reference them as `${CLAUDE_PLUGIN_ROOT}/scripts/<file>`. An installed plugin runs from a cache copy, so repo-relative or `~/.claude` paths break.
- Keep the README "Available skills" and "Available commands" tables and "Structure" tree in sync with what exists, in the same change that adds or removes a component.
- Keep the plugin name `hibatillah` identical in `plugin.json`, the `marketplace.json` plugin entry, and the README install command. The marketplace name is `hibatillah-agents`.
- Name components without the `hibatillah` prefix; the plugin namespace supplies it (`/hibatillah:tone`).

## Rules

- Write every agent file (skill, command, subagent, hook) in English. Example sentences inside a language file may be in that language.
- Keep every component free of personal and work information: no project, company, product, or colleague names, no facts from his work or life, no raw sentences copied from his messages. Examples are patterns and neutral templates with placeholders (A, B, X).
- When he edits a draft, log the correction in the skill's corrections log as a general pattern, not as the content of the edit. Check the log for private content before every commit.
- Change a skill's rules only with evidence from his own writing. Say when a rule is an inference.
- After changing rules in `skills/tone`, run `uv run skills/tone/check-voice.py` on a sample draft in each language to confirm the checker still agrees with the rules.
- Commit and push only when he asks.
