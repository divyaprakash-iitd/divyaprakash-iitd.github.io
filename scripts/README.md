# scripts/

Utility scripts for the Academic Pages template.

## `make-og-image.py`

Generates the default Open Graph / social preview image at
`images/og-image.png` (1200x630 PNG) used by `_includes/seo.html` when a page
does not define its own header image.

```
python3 scripts/make-og-image.py
```

Requirements:

- Python 3 with [Pillow](https://python-pillow.org) (`pip install Pillow`)
- A TrueType font; defaults to DejaVu Sans (`/usr/share/fonts/truetype/dejavu`),
  override with the `FONT_DIR` environment variable
- The site favicon at `images/favicon-512x512.png` (already in the template);
  it is composited as the card logo

The output is byte-reproducible for a given Pillow/font version and is committed
to the repo, so the build itself does not need Pillow.

## `make-favicons.py`

Rebuilds the favicon set in `images/` (`favicon-32x32.png`,
`favicon-192x192.png`, `favicon-512x512.png`, `favicon.ico` and
`apple-touch-icon-180x180.png`) from the logo at
`images/logo/dpcfd_mark_knockout.png`.

```
python3 scripts/make-favicons.py
```

Requires Python 3 with Pillow. After changing the icons, bump the `?v=` query
on the icon links in `_includes/head/custom.html` so browsers refetch them.
