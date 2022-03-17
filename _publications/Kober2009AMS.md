---
collection: publications
permalink: /conference/Kober2009AMS
pubtype: conference
author: "Kober, Jens and Peters, Jan"
title: "Learning new basic Movements for Robotics"
avenue: "Autonome Mobile Systeme (AMS)"
volume: 
number: 
pages: 105--112
year: 2009
bibtex: 
doi: "10.1007/978-3-642-10284-4_14"
file: "http://www.ias.informatik.tu-darmstadt.de/publications/paper_16.pdf"
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
