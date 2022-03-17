---
collection: publications
permalink: /conference/Franzese2020CoRL
pubtype: conference
author: "Franzese, Giovanni and Celemin, Carlos E. and Kober, Jens"
title: "Learning Interactively to Resolve Ambiguity in Reference Frame Selection"
avenue: "Proceedings of the 2020 Conference on Robot Learning"
volume: "155"
number: 
pages: 1298--1311
year: 2020
bibtex: 
doi: 
file: "https://proceedings.mlr.press/v155/franzese21a/franzese21a.pdf"
video: "https://youtu.be/tSQJP8Hpmbk"
code: 
website: "https://proceedings.mlr.press/v155/franzese21a.html"
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
