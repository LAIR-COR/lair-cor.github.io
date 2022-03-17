---
collection: publications
permalink: /preprint/Kober2012arXiv
pubtype: preprint
author: "Kober, Jens and Peters, Jan"
title: "Learning Prioritized Control of Motor Primitives"
avenue: 
volume: 
number: 
pages: 
year: 2012
bibtex: 
doi: 
file: "https://arxiv.org/pdf/1209.0488.pdf"
video: 
code: 
website: "https://arxiv.org/abs/1209.0488"
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
