---
collection: publications
permalink: /journal/PerezDattari2020RAM
pubtype: journal
author: "Perez-Dattari, Rodrigo and Celemin, Carlos E. and Franzese, Giovanni and Ruiz-del-Solar, Javier and Kober, Jens"
title: "Interactive Learning of Temporal Features for Control: Shaping Policies and State Representations From Human Feedback"
avenue: "IEEE Robotics & Automation Magazine"
volume: "27"
number: "2"
pages: 46--54
year: 2020
bibtex: 
doi: "10.1109/MRA.2020.2983649"
file: "http://www.jenskober.de/publications/PerezDattari2020RAM.pdf"
video: "https://youtu.be/4kWGfNdm21A"
code: "https://github.com/rperezdattari/Interactive-Learning-of-Temporal-Features-for-Control"
website: 
abstract: 
image: 
project: "flexcraft and teri"
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
