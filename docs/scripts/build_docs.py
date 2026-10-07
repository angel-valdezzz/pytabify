"""Build the bilingual manual and keyword reference."""

import shutil
from pathlib import Path

from bilingual_libdoc import generate
from bilingual_site import build

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    for config_dir in (ROOT, ROOT / "docs/config"):
        fonts = config_dir / ".cache/plugin/social/fonts/DejaVu Sans"
        fonts.mkdir(parents=True, exist_ok=True)
        for source in (ROOT / "docs/assets/fonts").glob("*.ttf"):
            shutil.copyfile(source, fonts / source.name)
    generate(
        "Pytabify",
        ROOT,
        "keywords/index.html",
        "https://angel-valdezzz.github.io/pytabify/",
    )
    build(ROOT)


if __name__ == "__main__":
    main()
