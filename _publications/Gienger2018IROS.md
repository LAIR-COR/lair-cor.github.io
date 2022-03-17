---
collection: publications
permalink: /conference/Gienger2018IROS
pubtype: conference
author: "Gienger, Michael and Ruiken, Dirk and Bates, Tamas and Regaieg, Mohamed and Meissner, Michael and Kober, Jens and Seiwald, Philipp and Hildebrandt, Arne-Christoph"
title: "Human-Robot Cooperative Object Manipulation with Contact Changes"
avenue: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)"
volume: 
number: 
pages: 1354--1360
year: 2018
bibtex: 
doi: "10.1109/IROS.2018.8594140"
file: "http://www.jenskober.de/publications/Gienger2018IROS.pdf"
video: "https://youtu.be/PO6cptKA2Qk"
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
