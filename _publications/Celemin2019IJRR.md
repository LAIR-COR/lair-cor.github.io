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