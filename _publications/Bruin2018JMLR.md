---
collection: publications
permalink: /journal/Bruin2018JMLR
pubtype: journal
author: "de Bruin, Tim and Kober, Jens and Tuyls, Karl and Babuska, Robert"
title: "Experience Selection in Deep Reinforcement Learning for Control"
avenue: "Journal of Machine Learning Research"
volume: "19"
number: "9"
pages: 1--56
year: 2018
bibtex: 
doi: 
file: "http://www.jenskober.de/publications/Bruin2018JMLR.pdf"
video: "https://youtu.be/Hli1ky0bgT4"
code: "https://github.com/timdebruin/baselines-experience-selection"
website: "http://jmlr.org/papers/v19/17-131.html"
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
