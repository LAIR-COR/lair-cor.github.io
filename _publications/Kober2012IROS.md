---
collection: publications
permalink: /conference/Kober2012IROS
pubtype: conference
author: "Kober, Jens and Muelling, Katharina and Peters, Jan"
title: "Learning Throwing and Catching Skills"
avenue: "IEEE/RSJ International Conference on Robot Systems (IROS), Video Track"
volume: 
number: 
pages: 5167--5168
year: 2012
bibtex: 
doi: "10.1109/iros.2012.6386267"
file: "http://www.ias.informatik.tu-darmstadt.de/uploads/Publications/Kober_IROS_2012.pdf"
video: "https://youtu.be/8tWh4jrcLBQ"
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
