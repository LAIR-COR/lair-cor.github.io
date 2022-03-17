---
collection: publications
permalink: /conference/Kober2009NIPS
pubtype: conference
author: "Kober, Jens and Peters, Jan"
title: "Policy Search for Motor Primitives in Robotics"
avenue: "Advances in Neural Information Processing Systems 21 (NIPS 2008)"
volume: 
number: 
pages: 849--856
year: 2009
bibtex: 
doi: 
file: "https://papers.nips.cc/paper/3545-policy-search-for-motor-primitives-in-robotics.pdf"
video: "https://youtu.be/cNyoMVZQdYM"
code: "http://jenskober.de/code.php"
website: "https://papers.nips.cc/paper/3545-policy-search-for-motor-primitives-in-robotics"
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
