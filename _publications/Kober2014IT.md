---
collection: publications
permalink: /journal/Kober2014IT
pubtype: journal
author: "Kober, Jens"
title: "Learning Motor Skills: From Algorithms to Robot Experiments"
avenue: "it - Information Technology"
volume: "56"
number: "3"
pages: 141--146
year: 2014
bibtex: 
doi: "10.1515/itit-2014-1039"
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
