---
collection: publications
permalink: /conference/Jauhri2020CoRL
pubtype: conference
author: "Jauhri, Snehal and Celemin, Carlos E. and Kober, Jens"
title: "Interactive Imitation Learning in State-Space"
avenue: "Proceedings of the 2020 Conference on Robot Learning (CoRL)"
volume: "155"
number: 
pages: 682--692
year: 2020
bibtex: 
doi: 
file: "https://proceedings.mlr.press/v155/jauhri21a/jauhri21a.pdf"
video: "https://youtu.be/mKgrBgat1PM"
code: "https://github.com/sjauhri/Interactive-Learning-in-State-space"
website: "https://proceedings.mlr.press/v155/jauhri21a.html"
abstract: 
image: 
project: "teri"
---
{% include base_path %}

{% if page.image %}
<p align="center">
{% if page.website %}
<a href="{{ page.website }}"> <img src="{{  page.image }}" alt="Logo skipped" style="max-height:200px"/> </a>
{% else %}
<img src="{{  page.image }}" alt="Logo skipped" />
{% endif %}
</p>
{% endif %}

{% if page.abstract %}
<p> <strong> <em> Abstract: </em> </strong> {{ page.abstract }}
    {% if page.webpage %}
        <a href="{{ page.website}}"> <br> More information </a>
    {% endif %}
</p>
{% endif %}
