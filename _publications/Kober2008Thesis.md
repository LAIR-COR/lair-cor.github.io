---
collection: publications
permalink: /other/Kober2008Thesis
pubtype: other
author: "Kober, Jens"
title: "Reinforcement Learning for Motor Primitives"
avenue: 
volume: 
number: 
pages: 
year: 2008
bibtex: 
doi: 
file: "http://www.ias.informatik.tu-darmstadt.de/publications/DiplomaThesis-Kober_5331[0].pdf"
video: "https://youtu.be/cNyoMVZQdYM"
code: "http://jenskober.de/code.php"
website: 
abstract: 
image: 
project: 
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
