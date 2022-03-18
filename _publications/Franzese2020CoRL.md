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
<a href="{{ page.website }}"> <img src="{{  page.image }}" alt="Paper Image not loaded." style="max-height:400px;max-width:400px"/> </a>
{% else %}
<img src="{{  page.image }}" alt="Paper Image not loaded." />
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


{% if page.video and page.video contains "embed" %}
<h2> Video </h2>
<div align="center">
<iframe width="420" height="315" src="{{ page.video }}" frameborder="0" allowfullscreen ></iframe>
</div>
{% endif %}


<div align="center" style="margin-top: 50px">
{% if page.doi %}
<button name="button" onclick="{{ page.doi }}" style="height:40px;width:100px">DOI</button>
{% endif %}
{% if page.file %}
<button name="button" onclick="{{ page.file }}" style="height:40px;width:100px">PDF</button>
{% endif %}
{% if page.video %}
<button name="button" onclick="{{ page.video }}" style="height:40px;width:100px">Video</button>
{% endif %}
{% if page.code %}
<button name="button" onclick="{{ page.code }}" style="height:40px;width:100px">Code</button>
{% endif %}
{% if page.website %}
<button name="button" onclick="{{ page.website }}" style="height:40px;width:100px">Site</button>
{% endif %}
</div>