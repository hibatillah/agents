# skills

Personal agent skills by Hibatillah.

## Skills

| Skill | What it does |
|---|---|
| [`hibatillah-tone`](skills/hibatillah-tone) | Writes or rewrites prose in Hibatillah's voice, in English (default) or Indonesian. |

## hibatillah-tone

A writing-style skill. It holds how he writes: the shape of a text, sentence habits, word choices, and what he avoids. It contains no facts about his work or life.

- `SKILL.md`: scope, language choice, and the rules shared by both languages.
- `en.md` and `id.md`: language-specific rules. English is the default.
- `examples.md` and `examples-id.md`: distilled patterns and neutral templates, plus a log of corrections.
- `check-voice.py`: a mechanical checker for both languages (dashes, hype words, chat words, spelling). It does not judge tone.

### Install

- **Claude Code:** copy `skills/hibatillah-tone` into `~/.claude/skills/` (or `~/.agents/skills/` for runtimes that read it).
- **claude.ai:** zip the `hibatillah-tone` folder (the folder itself at the top of the zip) and upload it under Settings, Capabilities, Skills.

### Check a draft

```
python skills/hibatillah-tone/check-voice.py draft.md
python skills/hibatillah-tone/check-voice.py --lang id draft.md
```

Exit code 1 means something was flagged.

### Using it as your own

The patterns are his. To make your own, replace the rules in `en.md` and `id.md` and the templates in the examples files with patterns from your own writing, and rename the skill.

## License

[MIT](LICENSE)
