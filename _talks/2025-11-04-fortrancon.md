---
title: "Modern Fortran for Fluid–Structure Simulations of Cilia and Particles"
collection: talks
type: "Talk"
talk_type: "Talk"
permalink: /talks/2025-11-fortrancon
venue: "FortranCon 2025"
date: 2025-11-04
location: "Online"
excerpt: "How modern Fortran structures a fluid–structure interaction solver for cilia and particles. Recorded; the video is on the talk page."
---
{% include base_path %}

How I built a fluid–structure interaction solver for cilia and particles in modern Fortran. The solver couples a 2D
incompressible Navier–Stokes solver with cilia modelled as flexible Kirchhoff rods and particles modelled with finite
elements, through the immersed boundary method. The talk shows how modules, object-oriented derived types, array
syntax, allocatable arrays and C interoperability (for GPU acceleration with NVIDIA AmgX) keep it maintainable,
extensible and fast.

<div class="talk-video">
  <iframe src="https://www.youtube-nocookie.com/embed/Oy_F4eK5dKk" title="Modern Fortran for Fluid–Structure Simulations of Cilia and Particles (FortranCon 2025)" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

[Watch on YouTube](https://www.youtube.com/watch?v=Oy_F4eK5dKk) ·
[Slides (PDF)]({{ base_path }}/files/talks/2025-11-fortrancon-slides.pdf) ·
[Cilia–particle simulation framework]({{ base_path }}/portfolio/portfolio-1/) ·
[Simulation gallery]({{ base_path }}/gallery/)
