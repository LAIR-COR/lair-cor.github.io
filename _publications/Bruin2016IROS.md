---
collection: publications
permalink: /conference/Bruin2016IROS
pubtype: conference
author: "de Bruin, Tim and Kober, Jens and Tuyls, Karl and Babuska, Robert"
title: "Improved Deep Reinforcement Learning for Robotics Through Distribution-based Experience Retention"
avenue: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)"
volume: 
number: 
pages: 3947--3952
year: 2016
bibtex: 
doi: "10.1109/iros.2016.7759581"
file: "http://www.jenskober.de/publications/Bruin2016IROS.pdf"
video: "https://youtu.be/yH7Vkr6taKg"
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
