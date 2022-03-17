---
collection: publications
permalink: /other/Kober2019ESC
pubtype: other
author: "Kober, Jens"
title: "Encyclopedia of Systems and Control"
avenue: 
volume: 
number: 
pages: 1--9
year: 2019
bibtex: 
doi: "10.1007/978-1-4471-5102-9_100027-1"
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
