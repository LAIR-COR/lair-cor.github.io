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
