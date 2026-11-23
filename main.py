"""Sleeve Notes for the Frog Trio -- writes one album title plus a short
back-cover blurb for a jazz trio made entirely of frogs to /output/entry.txt.

Stdlib only. No network, no third-party imports.
"""

from pathlib import Path

ENTRY = (
    "Pondwater Blue\n"
    "\n"
    "The Marshlight Trio \u2014 tenor sax, upright bass, brushes on snare \u2014 "
    "play where reeds meet still water at dusk. The sax leans low and "
    "unhurried, the bass walks the mudline, the drums fall like rain on "
    "leaves. Three frogs, one long evening, in no hurry to leave it. "
    "You can hear the room in it: wood, water, and the low hum of evening."
)


def main() -> None:
    # Gate guard: the entry must be 1-400 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars, must be 1-400"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    assert ENTRY.endswith("."), "entry must end with a period"
    # Title guard: the first line is the album title, followed by the blurb.
    assert ENTRY.split("\n", 1)[0] == "Pondwater Blue", "first line must be the title"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
