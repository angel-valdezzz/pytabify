"""Build the bilingual manual and keyword reference."""

from pathlib import Path

from bilingual_libdoc import generate
from bilingual_site import build

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    generate(
        "pytabify.robot.PyTabifyLibrary",
        ROOT,
        "keywords/index.html",
        "https://angel-valdezzz.github.io/pytabify/",
    )
    build(ROOT)


if __name__ == "__main__":
    main()
