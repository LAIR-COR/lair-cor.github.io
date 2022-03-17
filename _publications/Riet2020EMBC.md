---
collection: publications
permalink: /conference/Riet2020EMBC
pubtype: conference
author: "van Riet, Tom Cornelis Theodorus and de Graaf, Willem Mathys and van Antwerpen, Reinier and van Frankenhuyzen, Jan and de Lange, Jan and Kober, Jens"
title: "Robot Technology in Analyzing Tooth Removal -- a Proof of Concept"
avenue: "Annual International Conferences of the IEEE Engineering in Medicine & Biology Society (EMBC)"
volume: 
number: 
pages: 4721--4727
year: 2020
bibtex: 
doi: "10.1109/EMBC44109.2020.9176405"
file: "http://www.jenskober.de/publications/Riet2020EMBC.pdf"
video: 
code: 
website: 
abstract: 
image: 
project: "toothremoval"
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
