---
collection: publications
permalink: /conference/Manschitz2014IROS
pubtype: conference
author: "Manschitz, Simon and Kober, Jens and Gienger, Michael and Peters, Jan"
title: "Learning to Sequence Movement Primitives from Demonstrations"
avenue: "IEEE/RSJ Conference on Intelligent Robots and Systems (IROS)"
volume: 
number: 
pages: 4414--4421
year: 2014
bibtex: 
doi: "10.1109/iros.2014.6943187"
file: "http://www.ias.tu-darmstadt.de/uploads/Publications/Manschitz_IROS_2014.pdf"
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
