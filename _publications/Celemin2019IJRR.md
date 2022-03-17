---
collection: publications
permalink: /journal/Celemin2019IJRR
pubtype: journal
author: "Celemin, Carlos E. and Maeda, Guilherme and Ruiz-del-Solar, Javier and Peters, Jan and Kober, Jens"
title: "Reinforcement Learning of Motor Skills using Policy Search and Human Corrective Advice"
avenue: "International Journal of Robotics Research"
volume: "38"
number: "14"
pages: 1560--1580
year: 2019
bibtex: 
doi: "10.1177/0278364919871998"
file: "https://www.ias.informatik.tu-darmstadt.de/uploads/Alumni/JensKober/IJRR__Revision_.pdf"
video: "https://youtu.be/ptslNZdum2s"
code: 
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
