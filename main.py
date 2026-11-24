"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one sentence pitching a bizarre startup: trained
# mourners hired to weep at failed product launches, so investors see
# a packed room. Absurd at first glance, a real market on second look.
# One sentence, 125 characters — inside the 200-character gate.
# Revision note: the mourners are trained professionals, not actors;
# the paying customer is the founder, and the packed room is the payoff.
import os

TEXT = (
    "We rent trained mourners to weep at your failed product launch, "
    "so investors see a packed room and cry for the right reasons."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
