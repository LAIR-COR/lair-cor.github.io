---
collection: publications
permalink: /preprint/Wout2019arXiv
pubtype: preprint
author: "Wout, Daan and Scholten, Jan and Celemin, Carlos E. and Kober, Jens"
title: "Learning Gaussian Policies from Corrective Human Feedback"
avenue: 
volume: 
number: 
pages: 
year: 2019
bibtex: 
doi: 
file: "https://arxiv.org/pdf/1903.05216.pdf"
video: 
code: "https://github.com/DWout/GPC"
website: "https://arxiv.org/abs/1903.05216"
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
