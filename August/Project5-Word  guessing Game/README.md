# Word Guessing Game (Python CLI)

A minimal terminal game: guess the hidden word by entering either a single letter or the full word. You have 10 chances. A hint is shown for the chosen word.

# How it works

- A random word is chosen from a built‑in dictionary (word ➜ hint).
- Hint is printed as: `HINT: <hint>`.
- The word is masked using `_.` per character and printed as a single joined string.
- Each turn, enter:
  - a single letter (length = 1), or
  - the full word (length must match the word’s length).
- Correct letters reveal all matching positions.
- Repeated letter guesses are detected (no chance penalty).
- Win: guess the full word or reveal all letters.
- Lose: run out of 10 chances.


Note: Input is handled case‑insensitively (`.lower()`).

# Requirements

- Python 3.8+ (tested on 3.10.11; no external dependencies)

# Run

```bash
# Replace <filename>.py with your script name
python3 <filename>.py
# On Windows:
py <filename>.py