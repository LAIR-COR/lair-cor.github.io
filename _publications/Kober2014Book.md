---
collection: publications
permalink: /other/Kober2014Book
pubtype: other
author: "Kober, Jens and Peters, Jan"
title: "Learning Motor Skills - From Algorithms to Robot Experiments"
avenue: 
volume: "97"
number: 
pages: 
year: 2014
bibtex: 
doi: "10.1007/978-3-319-03194-1"
file: 
video: 
code: 
website: "http://link.springer.com/book/10.1007/978-3-319-03194-1"
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
