---
collection: publications
permalink: /conference/Peters2013Yale
pubtype: conference
author: "Peters, Jan and Kober, Jens and Muelling, Katharina and Nguyen-Tuong, Duy and Kroemer, Oliver"
title: "Learning Skills with Motor Primitives"
avenue: "16th Yale Learning Workshop"
volume: 
number: 
pages: 
year: 2013
bibtex: 
doi: 
file: 
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
