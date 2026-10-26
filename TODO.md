# Website to-do list

Improvement ideas from the October 2026 review. Kept in the repo but excluded from the site build (see `exclude` in `_config.yml`).

## 1. Reduce page weight (highest impact)
- [x] Portfolio excerpts converted to the same looping videos (`ellipsoidal_shell.gif` 36.6 MB -> 3.1 MB MP4,
      `cloud_py.png` 4.4 MB -> 416 KB WebP); the original animations have been deleted. Videos with class `lazy-play`
      play only while on screen (script in `_includes/footer/custom.html`).
- [x] Gallery: convert to looping MP4 videos (52 MB -> ~6 MB, all frames, same speed). Preview made in the
      Claude session; the home page thumbnails in `images/cfd_gallery/thumbs/` already use this approach
      (H.264, 560 px wide, original frame timing preserved).
- [x] Gallery (`_pages/gallery.md`) loads ~52 MB of animations. Biggest: `images/cfd_gallery/pwave.webp` (23 MB),
      `ibm_ellipse.webp` (5.5 MB), `fsi_beam.webp`, `ciliadnd.webp`, `channel_particle.webp`, `3d_particle.webp` (2–4 MB each).
      Re-encode at display size (~800 px wide) and a lower frame rate.
- [x] Home page artwork `images/DP_ECCOMAS_Pic.png` is 5642 px wide (1.6 MB) but shown at ~750 px. Serve a ~1600 px WebP
      and link the full-size file.
- [ ] Remove the remaining unused large files from `images/` after checking nothing links to them
      (e.g. `selected-cells.eps`; `cfd_gallery/donut_animation.webp` has been deleted).

## 2. Home page and sidebar
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

## 4. Later
- [ ] The template's sample "Terms and Privacy Policy" page was removed. The site uses Google Analytics, so consider a
      short privacy note of your own (what Analytics and the Giscus comments collect).
- [ ] Links: `.github/workflows/link-check.yml` checks every link monthly (and on demand from the Actions tab). Its
      report lists dead links; fix or remove them in the posts.
