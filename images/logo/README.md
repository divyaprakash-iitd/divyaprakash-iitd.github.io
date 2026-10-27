# dpcfd logo

The site's logo. Three finished files, all built from the same parametric TikZ drawing. The
bones are the original logo's: a two-turn spiral, an italic stem through its
centre, a crossbar, and an ascender on the outer end, so the "d", "p" and "f"
are still there. Three things changed to make it read as a vortex.

* **Logarithmic spiral.** The radius now grows by a constant factor per turn
  (`r = r_out * exp(-b * theta)`) instead of a constant amount, so the turns
  tighten toward the core the way a real vortex, a hurricane or a shell does.
  The old Archimedean spiral had evenly spaced turns and looked like a coil.
* **Width proportional to radius.** The band is 0.21 of the disc radius at the
  outer end and thins in proportion to the radius down to a fine tip at the
  core. Width and spacing shrink together, so every turn is a scaled copy of
  the last and the eye reads one continuous swirl.
* **Tapered ascender.** The "d" ascender narrows from the band width to a
  short tip, like a flick, instead of ending in a square block. The stem and
  crossbar keep a constant weight so the "p" and "f" stay legible.

The band edges are offset along the curve's true normal, so they stay parallel
to the centre line even in the tight inner turn. The spiral centre sits a
little right of and below the disc centre to balance the heavy outer sweep.

| File | Use |
| --- | --- |
| `dpcfd_mark.tex` | Black mark on the light-blue disc. Direct successor of the current logo. |
| `dpcfd_mark_knockout.tex` | White mark on a teal disc (`#2f7f93`, the site's primary colour). Where the stem and ascender leave the disc they invert to teal, so it works on white and on the dark theme without a halo. Best for favicons, app icons and social cards. |
| `dpcfd_mark_mono.tex` | Mark only, no disc. Recolour `dpmarkin` for white-on-dark or print. |

Each `.tex` has matching `.pdf`, `.svg` and transparent 600 dpi `.png` exports.
Every dimension is a named macro at the top of the file. Rebuild with:

```
pdflatex dpcfd_mark.tex
pdftocairo -svg dpcfd_mark.pdf dpcfd_mark.svg
pdftocairo -png -transp -r 600 -singlefile dpcfd_mark.pdf dpcfd_mark
```

## Where it is used

* `images/dpcfd_logo.png` is a 1000 px export of `dpcfd_mark`.
* The favicons, the Apple touch icon and the web-app manifest icons in
  `images/` are built from `dpcfd_mark_knockout.png` by
  `scripts/make-favicons.py`. Bump the `?v=` query on the icon links in
  `_includes/head/custom.html` after rebuilding them.
* The site header shows `images/masthead-logo.png`, also built by
  `scripts/make-favicons.py`, left of the site title (`_includes/masthead.html`,
  styled at the top of the site-specific section of `assets/css/main.scss`).
* The structured-data organisation logo in `_includes/seo.html` points at
  `images/favicon-512x512.png`.

## Other folders

* `explorations/` holds contact sheets of the directions tried on the way
  here: uniform stroke, taper toward the core, gradient disc, trailing
  streamline, pointed calligraphic stems, and several weights of the final
  design.
* `legacy/` holds the original logo (`dpcfd_logo_original.png`, with the
  wordmark) and its faithful TikZ recreation (`dpcfd_logo.tex`).
