---
collection: publications
permalink: /conference/Spaa2020ICRA
pubtype: conference
author: "van der Spaa, Linda F. and Bates, Tamas and Gienger, Michael and Kober, Jens"
title: "Predicting and Optimizing Ergonomics in Physical Human-Robot Cooperation Tasks"
avenue: "IEEE International Conference on Robotics and Automation (ICRA)"
volume: 
number: 
pages: 1799--1805
year: 2020
bibtex: 
doi: "10.1109/ICRA40945.2020.9197296"
file: "http://www.jenskober.de/publications/Spaa2020ICRA.pdf"
video: "https://youtu.be/D7zqglDkEq4"
code: 
website: 
abstract: 
image: 
project: "lphrct"
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