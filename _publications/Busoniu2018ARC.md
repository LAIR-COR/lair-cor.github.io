---
collection: publications
permalink: /journal/Busoniu2018ARC
pubtype: journal
author: "Buc soniu, Lucian and de Bruin, Tim and Tolic, Domagoj and Kober, Jens and Palunko, Ivana"
title: "Reinforcement Learning for Control: Performance, Stability, and Deep Approximators"
avenue: "Annual Reviews in Control"
volume: "46"
number: 
pages: 8--28
year: 2018
bibtex: 
doi: "10.1016/j.arcontrol.2018.09.005"
file: "http://www.jenskober.de/publications/Busoniu2018ARC.pdf"
video: 
code: 
website: 
abstract: 
image: 
project: "dl-force"
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
