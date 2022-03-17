---
collection: publications
permalink: /journal/Kober2011ML
pubtype: journal
author: "Kober, Jens and Peters, Jan"
title: "Policy Search for Motor Primitives in Robotics"
avenue: "Machine Learning"
volume: "84"
number: "1-2"
pages: 171--203
year: 2011
bibtex: 
doi: "10.1007/s10994-010-5223-6"
file: "http://www.ias.informatik.tu-darmstadt.de/uploads/Publications/kober_MACH_2011.pdf"
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
