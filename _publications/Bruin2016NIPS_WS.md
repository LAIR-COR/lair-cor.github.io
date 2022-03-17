---
collection: publications
permalink: /conference/Bruin2016NIPS_WS
pubtype: conference
author: "de Bruin, Tim and Kober, Jens and Tuyls, Karl and Babuska, Robert"
title: "Off Policy Experience Retention for Deep Actor Critic Learning"
avenue: "Deep Reinforcement Learning Workshop, Advances in Neural Information Processing Systems (NIPS)"
volume: 
number: 
pages: 
year: 2016
bibtex: 
doi: 
file: "http://www.jenskober.de/publications/Bruin2016NIPS_WS.pdf"
video: 
code: 
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
