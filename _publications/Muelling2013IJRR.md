---
collection: publications
permalink: /journal/Muelling2013IJRR
pubtype: journal
author: "Muelling, Katharina and Kober, Jens and Kroemer, Oliver and Peters, Jan"
title: "Learning to Select and Generalize Striking Movements in Robot Table Tennis"
avenue: "International Journal of Robotics Research"
volume: "32"
number: "3"
pages: 263--279
year: 2013
bibtex: 
doi: "10.1177/0278364912472380"
file: "http://www.ias.informatik.tu-darmstadt.de/uploads/Publications/Muelling_IJRR_2013.pdf"
video: "https://youtu.be/SH3bADiB7uQ"
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
