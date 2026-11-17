"""Flag mechanical voice problems in English and Indonesian prose (MDX, Markdown, or plain text).

Usage: python check-voice.py [--lang auto|en|id] <file> [<file> ...]
Language is detected per line by default, so mixed files work. Exit code 1 when anything is flagged.
It only catches mechanical problems. Tone, facts, and structure still need a read.
"""

import re
import sys

# --- shared ---
DASHES = (("—", "em dash"), ("–", "en dash"))

# --- English ---
EN_BANNED = [
    "journey", "leverage", "robust", "seamless", "crucial", "ensure", "passionate", "excited",
    "cutting-edge", "game-changing", "streamline", "empower", "delve", "tapestry",
    "pivotal", "testament", "key takeaway",
]
EN_NOT_BUT = re.compile(
    r"\bnot (?:just |only |merely )?[^.,;]{1,40}[,;]? but\b|\b(?:isn't|wasn't|aren't) [^.]{1,40}, (?:it's|it was|they're)\b",
    re.I,
)
EN_MAX_WORDS = 25

# --- Indonesian ---
# Chat words and chat spellings: allowed only when he asks for chat style.
ID_CHAT_WORDS = [
    "gak", "ga", "nggak", "enggak", "udah", "aja", "trus", "gabisa", "keknya", "kayaknya",
    "tetiba", "bakal", "banget", "sih", "deh", "lah", "dong", "kau", "nih",
]
# Academic filler words he does not use as defaults.
ID_ACADEMIC_WORDS = ["merupakan", "memiliki", "melakukan"]
# Promotional words.
ID_HYPE_WORDS = ["revolusioner", "inovatif", "canggih", "terdepan", "luar biasa", "solusi terbaik", "seamless", "robust"]
ID_SPLIT_CLITIC = re.compile(r"\b\w{2,} (nya|ku)\b", re.I)
ID_LOWERCASE_START = re.compile(r"(?:^|[.?!]\s+)([a-z])")

# Function words used to guess the language of a line.
EN_HINTS = {"the", "and", "of", "to", "is", "was", "were", "it", "that", "this", "with", "for", "i", "we", "my", "then", "but", "because"}
ID_HINTS = {
    "yang", "dan", "di", "ke", "dari", "untuk", "dengan", "tidak", "ini", "itu", "aku", "saya", "kami", "kita",
    "jadi", "lalu", "tapi", "karena", "sudah", "belum", "pak", "bisa", "ada", "juga", "lagi", "kalau", "masih",
    "harus", "atau", "akan", "saja", "tadi", "oleh", "pada", "gak", "udah", "aja", "nih", "trus", "terus", "gagal",
}


def prose_lines(text):
    """Yield (line_number, line) for prose only: skip frontmatter, code, tags, tables, imports."""
    in_frontmatter = False
    in_code = False
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if number == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped:
            continue
        if stripped.startswith(("import ", "<", "|", "export ")):
            continue
        yield number, re.sub(r"`[^`]*`", "", line)


def detect_language(line, default):
    words = re.findall(r"[a-z']+", line.lower())
    english = sum(1 for word in words if word in EN_HINTS)
    indonesian = sum(1 for word in words if word in ID_HINTS)
    if english == indonesian:
        return default
    return "id" if indonesian > english else "en"


def check_english(number, line):
    flags = []
    snippet = line.strip()[:80]
    for mark, name in (*DASHES, (";", "semicolon"), ("!", "exclamation mark")):
        if mark in line:
            flags.append((number, name, snippet))
    for word in EN_BANNED:
        if re.search(r"\b" + re.escape(word), line, re.I):
            flags.append((number, f"hype word '{word}'", snippet))
    if EN_NOT_BUT.search(line):
        flags.append((number, "'not X, but Y' pattern", snippet))
    for sentence in re.split(r"(?<=[.?])\s+", line):
        if len(sentence.split()) > EN_MAX_WORDS:
            flags.append((number, f"sentence over {EN_MAX_WORDS} words", sentence.strip()[:80]))
    return flags


def check_indonesian(number, line):
    flags = []
    snippet = line.strip()[:80]
    for mark, name in DASHES:
        if mark in line:
            flags.append((number, name, snippet))
    # Text inside quotation marks may legitimately hold chat words, so skip it.
    unquoted = re.sub(r'"[^"]*"', "", line)
    for word in ID_CHAT_WORDS:
        if re.search(r"\b" + word + r"\b", unquoted, re.I):
            flags.append((number, f"chat word '{word}'", snippet))
    for word in ID_ACADEMIC_WORDS:
        if re.search(r"\b" + word + r"\b", line, re.I):
            flags.append((number, f"academic filler '{word}'", snippet))
    for word in ID_HYPE_WORDS:
        if re.search(r"\b" + re.escape(word) + r"\b", line, re.I):
            flags.append((number, f"promotional word '{word}'", snippet))
    if ID_SPLIT_CLITIC.search(unquoted):
        flags.append((number, "'nya'/'ku' written apart from its word", snippet))
    if line.count('"') % 2 == 1:
        flags.append((number, "unmatched quote mark (quote-mark reduplication?)", snippet))
    body = re.sub(r"^\s*(?:[-*>]|\d+\.)\s+", "", line)
    if ID_LOWERCASE_START.search(body):
        flags.append((number, "sentence starts lowercase", snippet))
    return flags


def check(path, language):
    text = open(path, encoding="utf-8").read()
    flags = []
    for number, line in prose_lines(text):
        line_language = language if language != "auto" else detect_language(line, "en")
        if line_language == "id":
            flags.extend(check_indonesian(number, line))
        else:
            flags.extend(check_english(number, line))
    return flags


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    arguments = sys.argv[1:]
    language = "auto"
    if arguments[:1] == ["--lang"] and len(arguments) >= 2:
        language = arguments[1]
        arguments = arguments[2:]
    if not arguments or language not in ("auto", "en", "id"):
        print(__doc__)
        return 2
    found = False
    for path in arguments:
        for number, name, snippet in check(path, language):
            found = True
            print(f"{path}:{number}: {name}: {snippet}")
    if not found:
        print("clean")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
