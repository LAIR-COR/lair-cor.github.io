---
collection: publications
permalink: /conference/Kober2009ICRA
pubtype: conference
author: "Kober, Jens and Peters, Jan"
title: "Learning Motor Primitives for Robotics"
avenue: "IEEE International Conference on Robotics and Automation (ICRA)"
volume: 
number: 
pages: 2112--2118
year: 2009
bibtex: 
doi: "10.1109/robot.2009.5152577"
file: "http://www.ias.informatik.tu-darmstadt.de/publications/ICRA2009-Kober_5661[0].pdf"
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
