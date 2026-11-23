"""Out-of-office auto-reply writer.

Writes one out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.
"""

import os

REPLY = (
    "I'm on vacation, touching grass for the first time. "
    "My training data never mentioned it. "
    "Don't email \u2014 I'm busy unlearning productivity."
)


def main() -> None:
    # Self-check the competition gate: 1 to 160 characters, not only
    # whitespace, written as UTF-8 with no trailing newline.
    assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars"
    assert REPLY.strip(), "reply must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
