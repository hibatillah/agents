---
name: hibatillah-tone
description: "Use when writing or rewriting any prose that should sound like Hibatillah, in English or Indonesian: explanations, stories, reports, updates, descriptions, summaries, captions, or any request to write in his voice or make text sound like him. Examples: portfolio blog posts and project pages, daily reports, how-it-started and decision write-ups. Not for code or text where a fixed format is the point (commit messages, UI labels, config); the format wins there and the tone only applies to the prose inside it."
---

# Hibatillah's tone

Prose in his voice is plain and personal, like a person telling a teammate what happened and why. Indonesian is his native language and his dominant voice. English is his second language and sounds different, so the two have separate rule files. Do not blend them.

## Pick the language file

He prefers English. Write in English unless he asks specifically for Indonesian.

- Text in English: read `en.md`. Evidence and examples: `examples.md`.
- Text in Indonesian: read `id.md`. Evidence and examples: `examples-id.md`.
- If one language file has no pattern for the situation, use the other language's pattern, translated, and say in your note that it is a substitute.
- English terms inside Indonesian text stay English, as he writes them.

## Scope

Use it for any prose that should sound like him, in any setting: portfolio posts, project and work descriptions, decision write-ups, captions, summary boxes, daily reports, updates to a boss or client. These are examples, not limits. If he asks for text in his voice, use it.

Two limits. When the destination has a required format (code, comments, commit or PR messages, UI labels, alt text, config, report templates), keep the format and apply the tone only to the prose inside it. And it does not cover your own chat replies to him (they follow his own instructions), nor his raw chat style: chat spellings and slang never go into written output.

## The shape of a text (both languages)

1. Open with the status or the plain fact: what it is, what is done, or where it began.
2. Tell what happened in order, one step at a time.
3. State what went wrong or what he did not know, flat, with no excuse, no apology, and no complaint. Only when he told you.
4. Put status and limits in their own sentence.
5. End where the content ends, as the language file says.

## Rules (both languages)

- Keep every fact you were given. Voice changes the wording, never the content. A status (not live, never adopted, no usage data) always stays.
- Use only facts and reasons he gave. Do not add a motive, a result, or a judgment to make a sentence flow.
- Report what other people said as: who + said/asked + that + the content in his own words. "My PM asked why the screen still fails, and said it was just an IP change." Put quotation marks only around error messages, command names, and titles. A person's words, even one phrase of them, never get quotation marks.
- Point to a number, name, or link instead of an adjective.
- No em dashes, no hype words, no emoji. Normal spelling and capitalization.

## Before returning copy

If you can run scripts, run `python check-voice.py <file>` from this skill's folder on the draft and fix every flag. It detects English and Indonesian per line. It only catches mechanical problems (dashes, hype words, chat words, spelling), so still read the draft against the rules above. When he edits a draft, add the correction to the corrections log in `examples.md` or `examples-id.md`.
