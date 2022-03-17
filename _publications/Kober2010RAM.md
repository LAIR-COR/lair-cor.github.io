---
collection: publications
permalink: /journal/Kober2010RAM
pubtype: journal
author: "Kober, Jens and Peters, Jan"
title: "Imitation and Reinforcement Learning - Practical Algorithms for Motor Primitive Learning in Robotics"
avenue: "IEEE Robotics & Automation Magazine"
volume: "17"
number: "2"
pages: 55--62
year: 2010
bibtex: 
doi: "10.1109/mra.2010.936952"
file: "http://www.ias.informatik.tu-darmstadt.de/publications/kober_RAM_2010.pdf"
video: "https://youtu.be/cNyoMVZQdYM"
code: "http://jenskober.de/code.php"
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
