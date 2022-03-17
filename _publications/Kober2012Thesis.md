---
collection: publications
permalink: /other/Kober2012Thesis
pubtype: other
author: "Kober, Jens"
title: "Learning Motor Skills: From Algorithms to Robot Experiments"
avenue: 
volume: 
number: 
pages: 
year: 2012
bibtex: 
doi: 
file: "http://tuprints.ulb.tu-darmstadt.de/2992/1/DissertationKober.pdf"
video: 
code: 
website: "http://tuprints.ulb.tu-darmstadt.de/2992/"
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
