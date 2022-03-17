---
collection: publications
permalink: /conference/Feirstein2016PSYCO
pubtype: conference
author: "Feirstein, Denise S. and Koryakovskiy, Ivan and Kober, Jens and Vallery, Heike"
title: "Reinforcement Learning of Potential Fields to achieve Limit-Cycle Walking"
avenue: "IFAC International Workshop on Periodic Control Systems (PSYCO)"
volume: "49"
number: "14"
pages: 113--118
year: 2016
bibtex: 
doi: "10.1016/j.ifacol.2016.07.994"
file: "http://www.jenskober.de/publications/Feirstein2016IFAC.pdf"
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
