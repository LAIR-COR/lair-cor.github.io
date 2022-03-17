---
collection: publications
permalink: /preprint/Mazhar2021arXiv
pubtype: preprint
author: "Mazhar, Osama and Kober, Jens"
title: "Random Shadows and Highlights: A New Data Augmentation Method for Extreme Lighting Conditions"
avenue: 
volume: 
number: 
pages: 
year: 2021
bibtex: 
doi: 
file: "https://arxiv.org/pdf/2101.05361.pdf"
video: 
code: "https://github.com/OsamaMazhar/Random-Shadows-Highlights"
website: "https://arxiv.org/abs/2101.05361"
abstract: 
image: 
project: "opendr"
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
