# Website to-do list

Improvement ideas from the October 2026 review. Kept in the repo but excluded from the site build (see `exclude` in `_config.yml`).

## 1. Reduce page weight (highest impact)
- [ ] The home page now uses small thumbnails from `images/cfd_gallery/thumbs/` (made with Pillow: 560 px wide,
      at most 150 frames, quality 55). Do the same for the gallery page itself.
- [ ] Gallery (`_pages/gallery.md`) loads ~52 MB of animations. Biggest: `images/cfd_gallery/pwave.webp` (23 MB),
      `ibm_ellipse.webp` (5.5 MB), `fsi_beam.webp`, `ciliadnd.webp`, `channel_particle.webp`, `3d_particle.webp` (2–4 MB each).
      Re-encode at display size (~800 px wide) and a lower frame rate.
- [x] Home page artwork `images/DP_ECCOMAS_Pic.png` is 5642 px wide (1.6 MB) but shown at ~750 px. Serve a ~1600 px WebP
      and link the full-size file.
- [ ] Remove unused large files from `images/` (e.g. `ellipsoidal_shell.gif` 35 MB, `cfd_gallery/donut_animation.webp` 15 MB,
      `selected-cells.eps`, `cloud_py.png`) after checking nothing links to them.

## 2. Home page and sidebar
- [ ] Sidebar bio says "thesis submitted": change to the degree once it is awarded.
- [ ] The sidebar email is the IIT Delhi address; switch to a permanent one if that account closes.
- [x] Open the About page with one or two sentences about you and your research (who you are, IIT Delhi, immersed boundary
      methods / cilia–particle interaction), then the site description.
- [x] Drop the "This website is a work in progress" note.
- [x] Sidebar employer is cut off ("Indian Institute of Technolo…"): use "IIT Delhi" in `_config.yml` → `author.employer`.

## 3. Leftover template content
- [ ] Sample pages are still published and listed in the sitemap even though they're hidden from the menu:
      `_publications/` (Paper Title Number 1–5), `_talks/` (Talk 1–3, Tutorial 1), `_teaching/` (Teaching 1–2),
      plus `_pages/markdown.md`, `non-menu-page.md`, `archive-layout-with-content.md`, `terms.md`.
- [ ] Either replace them with real publications and talks (and add Publications/Talks back to `_data/navigation.yml`),
      or delete them.

## Notes for future template updates
- Upstream template: https://github.com/academicpages/academicpages.github.io (last merged at 7b95833, Oct 2026).
- Site-specific styling lives in `_sass/theme/_dpcfd_light.scss`, `_sass/theme/_dpcfd_dark.scss` and the
  "Site-specific styles" section at the end of `assets/css/main.scss`. Keep custom changes there to make merges easy.
- Deployment is via GitHub Actions (`.github/workflows/jekyll.yml`); the classic Pages builder can't compile the template's Sass.
- `url` in `_config.yml` must stay `https://dpcfd.com`, or the JavaScript (theme toggle, menu) is blocked by the redirect.
