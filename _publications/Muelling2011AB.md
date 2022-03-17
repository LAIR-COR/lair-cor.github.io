---
collection: publications
permalink: /journal/Muelling2011AB
pubtype: journal
author: "Muelling, Katharina and Kober, Jens and Peters, Jan"
title: "A Biomimetic Approach to Robot Table Tennis"
avenue: "Adaptive Behavior"
volume: "19"
number: "5"
pages: 359--376
year: 2011
bibtex: 
doi: "10.1177/1059712311419378"
file: "http://www.ias.informatik.tu-darmstadt.de/publications/Muelling_ABJ2011.pdf"
video: "https://youtu.be/BcJ4S4L1n78"
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
