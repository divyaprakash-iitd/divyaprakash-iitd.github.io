#!/usr/bin/env python3
"""Build the site's favicon set from the dpcfd knockout mark.

Source: images/logo/dpcfd_mark_knockout.png, the transparent 600 dpi export of
images/logo/dpcfd_mark_knockout.tex (white vortex on a teal disc).

Writes, into images/:
  favicon-32x32.png, favicon-192x192.png, favicon-512x512.png  transparent
  favicon.ico                                                  16, 32 and 48 px
  apple-touch-icon-180x180.png                                 opaque white ground,
                                                               since iOS fills
                                                               transparency with black

Usage:  python3 scripts/make-favicons.py
"""
import os

from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(REPO_ROOT, "images")
SOURCE = os.path.join(IMAGES, "logo", "dpcfd_mark_knockout.png")


def icon(mark, size, pad, background=(0, 0, 0, 0)):
    """Fit the mark into a size x size square, `pad` being the margin fraction."""
    inner = max(1, round(size * (1 - 2 * pad)))
    m = mark.copy()
    m.thumbnail((inner, inner), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), background)
    canvas.alpha_composite(m, ((size - m.width) // 2, (size - m.height) // 2))
    return canvas


def main():
    mark = Image.open(SOURCE).convert("RGBA")
    mark = mark.crop(mark.getbbox())

    # Tiny icons get almost no margin so the disc stays as large as possible.
    for size, pad in ((32, 0.0), (192, 0.02), (512, 0.02)):
        icon(mark, size, pad).save(os.path.join(IMAGES, f"favicon-{size}x{size}.png"), optimize=True)

    ico = [icon(mark, s, 0.0) for s in (48, 32, 16)]
    ico[0].save(os.path.join(IMAGES, "favicon.ico"), sizes=[(48, 48), (32, 32), (16, 16)],
                append_images=ico[1:])

    apple = icon(mark, 180, 0.08, background=(255, 255, 255, 255)).convert("RGB")
    apple.save(os.path.join(IMAGES, "apple-touch-icon-180x180.png"), optimize=True)


if __name__ == "__main__":
    main()
