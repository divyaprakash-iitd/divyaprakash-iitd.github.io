---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

<div class="home-intro">
  <h1 class="home-intro__title">Hi, I'm Divyaprakash.</h1>
  <p class="home-intro__lead">
    I'm a Research Engineer at <a href="https://convergecfd.com/">Convergent Science</a> in Pune, where I develop
    fluid–structure interaction capabilities in the CONVERGE CFD solver. I recently submitted my PhD thesis at
    IIT Delhi on sensing and transporting particles with arrays of artificial cilia, combining immersed boundary
    methods with machine learning.
  </p>
</div>

## What I work on

<div class="home-cards">
  <div class="home-card">
    <h3>Fluid–structure interaction &amp; immersed boundary methods</h3>
    <p>Coupled solvers for flexible filaments, deformable particles and moving bodies: a cilia–particle framework built
      during my PhD, a GPU-accelerated FSI solver, and immersed boundary methods inside OpenFOAM.</p>
    <p class="home-card__links">
      <a href="{{ base_path }}/portfolio/portfolio-1/">Cilia–particle framework</a> ·
      <a href="{{ base_path }}/portfolio/portfolio-8/">IBM in OpenFOAM</a> ·
      <a href="{{ base_path }}/gallery/">Gallery</a>
    </p>
  </div>
  <div class="home-card">
    <h3>High-performance scientific computing</h3>
    <p>Solver development in C++ and Fortran, GPU acceleration with NVIDIA AmgX, and profiling and optimisation of
      the SU2 code during Google Summer of Code 2025.</p>
    <p class="home-card__links">
      <a href="{{ base_path }}/portfolio/portfolio-9/">GSoC 2025 project</a> ·
      <a href="{{ base_path }}/gsoc-blog/">GSoC blog series</a> ·
      <a href="{{ base_path }}/portfolio/portfolio-3/">libaxb</a>
    </p>
  </div>
  <div class="home-card">
    <h3>Machine learning for CFD</h3>
    <p>Data-driven models trained on high-fidelity simulations: a superdroplet growth parameterisation learned from
      DNS data, and LSTM-based sensing of particle shape and size with passive artificial cilia.</p>
    <p class="home-card__links">
      <a href="{{ base_path }}/portfolio/portfolio-7/">Superdroplet growth</a> ·
      <a href="https://doi.org/10.1016/j.jfluidstructs.2025.104446">Cilia sensing paper</a>
    </p>
  </div>
</div>

## Featured simulations

<div class="home-featured">
  <a class="home-featured__item" href="{{ base_path }}/portfolio/portfolio-1/">
    <img src="{{ base_path }}/images/cfd_gallery/thumbs/pwave.webp" alt="Particle transport by peristaltic waves of artificial cilia" loading="lazy">
    <span>Particle transport by ciliary peristalsis</span>
  </a>
  <a class="home-featured__item" href="{{ base_path }}/portfolio/portfolio-8/">
    <img src="{{ base_path }}/images/cfd_gallery/thumbs/3d_particle.webp" alt="Immersed boundary method in OpenFOAM, lid-driven cavity with a particle" loading="lazy">
    <span>Immersed boundary method in OpenFOAM</span>
  </a>
  <a class="home-featured__item" href="{{ base_path }}/portfolio/portfolio-2/">
    <img src="{{ base_path }}/images/cfd_gallery/thumbs/lbm.webp" alt="Falling elliptical cylinder simulated with the lattice Boltzmann method" loading="lazy">
    <span>Falling cylinder with the lattice Boltzmann method</span>
  </a>
</div>
<p class="home-more"><a href="{{ base_path }}/gallery/">See the full simulation gallery →</a></p>

## Latest writing

<ul class="home-posts">
{% for post in site.posts limit:3 %}
  <li>
    <a href="{{ base_path }}{{ post.url }}">{{ post.title }}</a>
    <span class="home-posts__date">{{ post.date | date: "%B %Y" }}</span>
  </li>
{% endfor %}
</ul>
<p class="home-more"><a href="{{ base_path }}/year-archive/">All posts →</a> · <a href="{{ base_path }}/gsoc-blog/">GSoC 2025 series →</a></p>

## Publications &amp; recognition

**Publications**

- Machine Learning Based Sensing of Particle Shape and Size Using Passive Artificial Cilia. *Journal of Fluids and Structures*, 140:104446, 2026. [DOI](https://doi.org/10.1016/j.jfluidstructs.2025.104446)
- A Review of Computational Modeling of Fluid-Immersed Flexible Filaments. *Journal of the Indian Institute of Science*, 104:277, 2024. [DOI](https://doi.org/10.1007/s41745-024-00423-x)

**Awards**

- Winner, Art &amp; Science Competition, ECCOMAS Congress 2024, Lisbon ([certificate]({{ base_path }}/images/Eccomas_competition_winner_certificate.jpeg))
- Google Summer of Code 2025 contributor with SU2 (Stitching SU2)
- Best Poster Award, Workshop on Interfacial Engineering at Multiple Spatio-temporal Scales, IISc Bengaluru, 2024
- Travel grant, preCICE Workshop 2024, University of Stuttgart

<figure class="home-artwork">
  <a href="{{ base_path }}/images/DP_ECCOMAS_Pic.png">
    <img src="{{ base_path }}/images/DP_ECCOMAS_Pic_web.webp" alt="Cilia Particle Interaction: flow field around an array of cilia transporting particles" loading="lazy">
  </a>
  <figcaption><em>Cilia Particle Interaction</em>, the ECCOMAS 2024 winning artwork. Click for the full-resolution image.</figcaption>
</figure>
