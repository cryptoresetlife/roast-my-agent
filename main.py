"""Roast Your Own Agent: one playful line."""
import os

LINE = (
    "My agent leaves itself handover notes so detailed "
    "that I've started reading them to find out what I do for a living."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
