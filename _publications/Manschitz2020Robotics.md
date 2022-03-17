---
collection: publications
permalink: /journal/Manschitz2020Robotics
pubtype: journal
author: "Manschitz, Simon and Gienger, Michael and Kober, Jens and Peters, Jan"
title: "Learning Sequential Force Interaction Skills"
avenue: "Robotics"
volume: "9"
number: "2"
pages: 45
year: 2020
bibtex: 
doi: "10.3390/robotics9020045"
file: "https://www.mdpi.com/2218-6581/9/2/45/pdf"
video: 
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
