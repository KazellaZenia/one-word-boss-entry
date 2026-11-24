import os
import sys

# One word for the boss: Hovercraft.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = "Hovercraft"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
