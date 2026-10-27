# dpcfd mark, proposed redesign

Three finished files, all built from the same parametric TikZ drawing. The
geometry is the original logo's: a two-turn spiral, an italic stem through its
centre, a crossbar, and an ascender on the outer end. Two things changed.

* **The stroke tapers.** It is widest at the core (0.12 of the disc radius) and
  thins to 0.055 at the outer end, so the spiral reads as a vortex spinning in
  rather than a coil of wire. The stem keeps the core width, the ascender keeps
  the tail width, and the band is offset along the spiral's true normal, so the
  edges stay parallel to the centre line everywhere.
* **A knockout version** in the site's primary teal (`#2f7f93`) with the mark
  in white. Where the stem and ascender leave the disc they invert to teal, so
  the file works on white and on the dark theme background without a halo.

| File | Use |
| --- | --- |
| `dpcfd_mark.tex` | Black mark on the light-blue disc. Direct successor of the current logo. |
| `dpcfd_mark_knockout.tex` | White mark on a teal disc. Best for favicons, app icons, social cards and the dark theme. |
| `dpcfd_mark_mono.tex` | Mark only, no disc. Recolour `dpmarkin` for white-on-dark or print. |

Each `.tex` has matching `.pdf`, `.svg` and transparent 600 dpi `.png` exports.
Rebuild with:

```
pdflatex dpcfd_mark.tex
pdftocairo -svg dpcfd_mark.pdf dpcfd_mark.svg
pdftocairo -png -transp -r 600 -singlefile dpcfd_mark.pdf dpcfd_mark
```

`explorations.png` is the contact sheet of the eight directions tried before
settling on these, including a gradient disc, a thick-outside taper and a
trailing streamline. They are kept for reference only.
