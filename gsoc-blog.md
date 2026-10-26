---
layout: archive
title: "My Google Summer of Code (GSoC 2025) Journey"
permalink: /gsoc-blog/
author_profile: true
---

{% include base_path %}

In summer 2025 I took part in Google Summer of Code with **Stitching SU2**, working on the project ["**Using Data-Driven, Physics-Informed Machine Learning to Model Fluid Properties in Computational Fluid Dynamics**"](https://summerofcode.withgoogle.com/programs/2025/projects/iFt1m8Wx). These posts chronicle my weekly progress, challenges and learnings during the program.

<div class="gsoc-outcome">
  <p><strong>Outcome:</strong> profiling support and performance improvements to SU2's MLPCpp neural-network module, including a 1.3× speedup of network evaluation in tests.</p>
  <p><a href="https://gist.github.com/divyaprakash-iitd/998eaf88bcc1b1325c29a53dca8a3e91">Read the final project summary</a> (results, benchmarks and future work) · <a href="{{ base_path }}/portfolio/portfolio-9/">Project overview</a></p>
</div>

## About the project
The project aimed to enhance SU2’s CFD capabilities by optimizing the MLPCpp neural-network module in the Non-Ideal Compressible Fluid Dynamics framework, through performance improvements and better inverse regression, delivered as a tutorial and a code update with benchmarks.

## Weekly posts

{% comment %} site.posts is newest first; the series reads from the start, so reverse it. {% endcomment %}
{% assign gsoc_posts = site.posts | where_exp: "post", "post.categories contains 'GSoC'" | reverse %}
<ol class="gsoc-timeline">
{% for post in gsoc_posts %}
  {% assign title_parts = post.title | split: ":" %}
  {% assign step = title_parts | first | remove: "GSoC" | strip %}
  {% assign heading = post.title | remove_first: title_parts[0] | remove_first: ":" | strip %}
  {% if heading == "" %}{% assign heading = post.title %}{% endif %}
  <li class="gsoc-timeline__item">
    <span class="gsoc-timeline__step">{{ step }}</span>
    <div class="gsoc-timeline__body">
      <h3 class="gsoc-timeline__title"><a href="{{ base_path }}{{ post.url }}">{{ heading }}</a></h3>
      <p class="gsoc-timeline__date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time></p>
      {% assign raw = post.excerpt | strip %}
      {% assign first_char = raw | slice: 0 %}{% if first_char == "<" %}{% assign summary = raw | strip_html | strip %}{% else %}{% assign summary = raw | escape %}{% endif %}
      {% if summary != "" %}<p class="gsoc-timeline__summary">{{ summary | truncatewords: 32 }}</p>{% endif %}
    </div>
  </li>
{% endfor %}
</ol>
