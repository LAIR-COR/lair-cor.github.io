---
collection: publications
permalink: /preprint/Meszaros2021arXiv
pubtype: preprint
author: "Meszaros, Anna and Franzese, Giovanni and Kober, Jens"
title: "Teaching Robots to Grasp Like Humans: An Interactive Approach"
avenue: 
volume: 
number: 
pages: 
year: 2021
bibtex: 
doi: 
file: "https://arxiv.org/pdf/2110.04534.pdf"
video: "https://youtu.be/6brynHStxGE"
code: 
website: "https://arxiv.org/abs/2110.04534"
abstract: 
image: 
project: "teri and airlab"
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
