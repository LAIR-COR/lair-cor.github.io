---
collection: publications
permalink: /conference/Bruin2020IFAC
pubtype: conference
author: "de Bruin, Tim and Kober, Jens and Tuyls, Karl and Babuska, Robert"
title: "Fine-tuning Deep RL with Gradient-Free Optimization"
avenue: "21th IFAC World Congress"
volume: "53"
number: "2"
pages: 8049-8056
year: 2020
bibtex: 
doi: "10.1016/j.ifacol.2020.12.2240"
file: "http://www.jenskober.de/publications/Bruin2020IFAC.pdf"
video: 
code: "https://github.com/timdebruin/drl-gradient-free-finetuning"
website: 
abstract: 
image: 
project: "dl-force"
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
