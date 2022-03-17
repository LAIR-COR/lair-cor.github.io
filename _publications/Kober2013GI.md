---
collection: publications
permalink: /conference/Kober2013GI
pubtype: conference
author: "Kober, Jens"
title: "Lernen Motorischer Fahigkeiten: Von Algorithmen zu Roboter-Experimenten"
avenue: "Ausgezeichnete Informatikdissertationen 2012"
volume: 
number: 
pages: 181--190
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
