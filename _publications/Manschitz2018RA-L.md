---
collection: publications
permalink: /journal/Manschitz2018RA-L
pubtype: journal
author: "Manschitz, Simon and Gienger, Michael and Kober, Jens and Peters, Jan"
title: "Mixture of Attractors: A Novel Movement Primitive Representation for Learning Motor Skills From Demonstrations"
avenue: "IEEE Robotics and Automation Letters"
volume: "3"
number: "2"
pages: 926--933
year: 2018
bibtex: 
doi: "10.1109/LRA.2018.2792531"
file: "http://www.ias.tu-darmstadt.de/uploads/Team/SimonManschitz/ManschitzRAL2018.pdf"
video: "https://youtu.be/cmR53SXqB-8"
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
