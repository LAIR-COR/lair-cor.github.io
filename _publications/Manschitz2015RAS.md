---
collection: publications
permalink: /journal/Manschitz2015RAS
pubtype: journal
author: "Manschitz, Simon and Kober, Jens and Gienger, Michael and Peters, Jan"
title: "Learning Movement Primitive Attractor Goals and Sequential Skills from Kinesthetic Demonstrations"
avenue: "Robotics and Autonomous Systems"
volume: "74"
number: "Part A"
pages: 97--107
year: 2015
bibtex: 
doi: "10.1016/j.robot.2015.07.005"
file: "http://www.ias.tu-darmstadt.de/uploads/Site/EditPublication/ManschitzRAS2015.pdf"
video: "https://youtu.be/WCayQ8xIiU8"
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
