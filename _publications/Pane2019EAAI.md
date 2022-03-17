---
collection: publications
permalink: /journal/Pane2019EAAI
pubtype: journal
author: "Pane, Yudha Prawira and Nageshrao, Subramanya Prasad and Kober, Jens and Babuska, Robert"
title: "Reinforcement Learning Based Compensation Methods for Robot Manipulators"
avenue: "Engineering Applications of Artificial Intelligence"
volume: "78"
number: 
pages: 236--247
year: 2019
bibtex: 
doi: "10.1016/j.engappai.2018.11.006"
file: "http://www.jenskober.de/publications/Pane2019EAAI.pdf"
video: "https://youtu.be/FzvTGfxCi3I"
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
