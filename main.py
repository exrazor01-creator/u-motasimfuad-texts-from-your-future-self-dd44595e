"""Texts From Your Future Self -- make.fun one-liner entry.

The line is a text from the writer's future self, ten years on, written
exactly as it would arrive on a phone: short, blunt, no setup. The joke
turns on two small domestic failures that are still haunting the future
self a decade later -- ten years spent watering a plant that was never
alive, and a camera roll so full of screenshots that nothing can ever
be found in it. The twist is that the future self is not wiser or
fixed; they are still living with the same mess, which is what makes
the warning feel like a real text from a real person rather than a
fortune-cookie line. Every detail is specific (the plastic plant, the
ten wasted years, the 4,000 screenshots, the year 2036), the punchline
lands on the last clause, and it avoids the obvious broke-or-tired
angle entirely.
"""

import os

# The entry: a text from the future self, ten years on.
# The plastic plant is the first beat -- ten years of watering something
# that never needed water, stated as a flat accusation. The screenshots
# are the second beat: the future self is still drowning in the same
# camera roll, so the warning is less advice and more a shared complaint
# from someone who knows exactly how it ends.
LINE = "Hey, it's you from 2036. You've been watering a plastic plant for ten years. Delete the 4,000 screenshots, I still can't find anything either."


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 200 characters, with no leading or trailing space, no
    double spaces, and no control or non-printable characters (only
    printable ASCII, code points 32-126, is allowed).
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if not all(32 <= ord(ch) <= 126 for ch in text):
        raise ValueError("entry must contain only printable ASCII characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
