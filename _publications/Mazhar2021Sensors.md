---
collection: publications
permalink: /journal/Mazhar2021Sensors
pubtype: journal
author: "Mazhar, Osama and Ramdani, Sofiane and Cherubini, Andrea"
title: "A Deep Learning Framework for Recognizing Both Static and Dynamic Gestures"
avenue: "Sensors"
volume: "21"
number: "6"
pages: 
year: 2021
bibtex: 
doi: "10.3390/s21062227"
file: "https://www.mdpi.com/1424-8220/21/6/2227/pdf"
video: "https://youtu.be/lB5vXc8LMnk"
code: 
website: 
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
