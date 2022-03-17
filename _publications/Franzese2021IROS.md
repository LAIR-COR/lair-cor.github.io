---
collection: publications
permalink: /conference/Franzese2021IROS
pubtype: conference
author: "Franzese, Giovanni and Meszaros, Anna and Peternel, Luka and Kober, Jens"
title: "ILoSA: Interactive Learning of Stiffness and Attractors"
avenue: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)"
volume: 
number: 
pages: 7778--7785
year: 2021
bibtex: 
doi: "10.1109/IROS51168.2021.9636710"
file: "http://www.jenskober.de/publications/Franzese2021IROS.pdf"
video: "https://youtu.be/MAG-kFGztws"
code: 
website: "https://arxiv.org/abs/2103.03099"
abstract: 
image: 
project: "teri"
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
