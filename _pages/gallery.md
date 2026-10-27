---
layout: archive
title: "Simulation Gallery"
permalink: /gallery/
author_profile: true
---

{% include base_path %}

<p class="gallery-intro">Simulations from my research and earlier projects, grouped by topic. Each clip plays while it is on screen; use <em>Full size</em> to open the video on its own.</p>

{% comment %} Content lives in _data/gallery.yml. Clips wider than 2:1 span both columns. {% endcomment %}
{% for group in site.data.gallery %}
<section class="gallery-group">
  <h2 class="gallery-group__title" id="{{ group.group | slugify }}">{{ group.group }}</h2>
  <div class="gallery-grid">
  {% for item in group.items %}
    {% assign ratio = item.width | times: 1.0 | divided_by: item.height %}
    {% assign src = base_path | append: "/images/cfd_gallery/video/" | append: item.video %}
    <figure class="gallery-item{% if ratio > 2 %} gallery-item--wide{% endif %}">
      <video class="lazy-play" src="{{ src }}.mp4" poster="{{ src }}.jpg" width="{{ item.width }}" height="{{ item.height }}"
             muted loop playsinline preload="none" controls aria-label="{{ item.title }}"></video>
      <figcaption>
        <h3 class="gallery-item__title">{{ item.title }}</h3>
        <p class="gallery-item__tags"><span class="gallery-item__year">{{ item.year }}</span>{% for tool in item.tools %}<span class="gallery-item__tool">{{ tool }}</span>{% endfor %}</p>
        {% if item.caption %}<p class="gallery-item__caption">{{ item.caption }}</p>{% endif %}
        <p class="gallery-item__links">
          {% for link in item.links %}{% assign first = link.url | slice: 0 %}<a href="{% if first == '/' %}{{ base_path }}{% endif %}{{ link.url }}">{{ link.label }}</a><span class="gallery-item__sep">·</span>{% endfor %}<a href="{{ src }}.mp4">Full size</a>
        </p>
      </figcaption>
    </figure>
  {% endfor %}
  </div>
</section>
{% endfor %}
