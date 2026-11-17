# CLAUDE.md

Guidance for agents working in this repo. It holds agent skills; the first is `skills/hibatillah-tone`.

## Rules

- Skill files are written in English. Example sentences inside a language file may be in that language.
- Keep every skill free of personal and work information: no project, company, product, or colleague names, no facts from his work or life, no raw sentences copied from his messages. Examples are patterns and neutral templates with placeholders (A, B, X).
- When he edits a draft, log the correction in the skill's corrections log as a general pattern, not as the content of the edit. Check the log for private content before every commit.
- Change a skill's rules only with evidence from his own writing. Say when a rule is an inference.
- After changing rules in `skills/hibatillah-tone`, run `python skills/hibatillah-tone/check-voice.py` on a sample draft in each language to confirm the checker still agrees with the rules.
- Do not commit or push unless he asks.
