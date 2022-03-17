---
collection: publications
permalink: /journal/Kober2012Auro
pubtype: journal
author: "Kober, Jens and Wilhelm, Andreas and Oztop, Erhan and Peters, Jan"
title: "Reinforcement Learning to Adjust Parametrized Motor Primitives to New Situations"
avenue: "Autonomous Robots"
volume: "33"
number: "4"
pages: 361--379
year: 2012
bibtex: 
doi: "10.1007/s10514-012-9290-3"
file: "http://www.ias.informatik.tu-darmstadt.de/uploads/Publications/kober_auro2012.pdf"
video: "https://youtu.be/C63avx1YCF4"
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
