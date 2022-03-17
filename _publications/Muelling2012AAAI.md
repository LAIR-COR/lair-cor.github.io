---
collection: publications
permalink: /conference/Muelling2012AAAI
pubtype: conference
author: "Muelling, Katharina and Kober, Jens and Kroemer, Oliver and Peters, Jan"
title: "Learning to Select and Generalize Striking Movements in Robot Table Tennis"
avenue: "AAAI Fall Symposium on Robots that Learn Interactively from Human Teachers"
volume: 
number: 
pages: 263--279
year: 2012
bibtex: 
doi: 
file: "http://www.jenskober.de/publications/Muelling2012AAAI.pdf"
video: "https://youtu.be/SH3bADiB7uQ"
code: 
website: "http://www.aaai.org/ocs/index.php/FSS/FSS12/paper/view/5602"
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
