---
collection: publications
permalink: /conference/Rastogi2018ICRA_WS
pubtype: conference
author: "Rastogi, Divyam and Koryakovskiy, Ivan and Kober, Jens"
title: "Sample-efficient Reinforcement Learning via Difference Models"
avenue: "Third Machine Learning in Planning and Control of Robot Motion Workshop at IEEE International Conference on Robotics and Automation (ICRA)"
volume: 
number: 
pages: 
year: 2018
bibtex: 
doi: 
file: "http://www.jenskober.de/publications/Rastogi2018ICRA_WS.pdf"
video: "https://youtu.be/rVIpd0qtaWA"
code: 
website: "https://www.cs.unm.edu/amprg/Workshops/MLPC18/schedule.html"
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
