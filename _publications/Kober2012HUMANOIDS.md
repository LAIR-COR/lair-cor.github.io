---
collection: publications
permalink: /conference/Kober2012HUMANOIDS
pubtype: conference
author: "Kober, Jens and Glisson, Matthew and Mistry, Michael"
title: "Playing Catch and Juggling with a Humanoid Robot"
avenue: "IEEE-RAS International Conference on Humanoid Robots (HUMANOIDS)"
volume: 
number: 
pages: 875--881
year: 2012
bibtex: 
doi: "10.1109/humanoids.2012.6651623"
file: "http://www.ias.informatik.tu-darmstadt.de/publications/Kober_Humanoids_2012.pdf"
video: "https://youtu.be/83eGcht7IiI"
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
