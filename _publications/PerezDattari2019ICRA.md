---
collection: publications
permalink: /conference/PerezDattari2019ICRA
pubtype: conference
author: "Perez-Dattari, Rodrigo and Celemin, Carlos E. and Ruiz-del-Solar, Javier and Kober, Jens"
title: "Continuous Control for High-Dimensional State Spaces: An Interactive Learning Approach"
avenue: "IEEE International Conference on Robotics and Automation (ICRA)"
volume: 
number: 
pages: 7611--7617
year: 2019
bibtex: 
doi: "10.1109/ICRA.2019.8793675"
file: "http://www.jenskober.de/publications/PerezDattari2019ICRA.pdf"
video: "https://youtu.be/i4f1D4CH26E"
code: "https://github.com/rperezdattari/Continuous-Control-for-High-Dimensional-State-Spaces-An-Interactive-Learning-Approach"
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
