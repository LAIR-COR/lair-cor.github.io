---
collection: publications
permalink: /journal/Zhu2022RA-L
pubtype: journal
author: "Zhu, Jihong and Gienger, Michael and Kober, Jens"
title: "Learning Task-Parameterized Skills from Few Demonstrations"
avenue: "IEEE Robotics and Automation Letters"
volume: 
number: 
pages: 
year: 2022
bibtex: 
doi: "10.1109/LRA.2022.3150013"
file: "https://arxiv.org/pdf/2201.09975.pdf"
video: "https://youtu.be/yY4k1nnhA60"
code: "https://github.com/Jihong-Zhu/learning-tp-skills-from-few-demos"
website: "https://sites.google.com/view/tp-gmm-from-few-demos/"
abstract: 
image: 
project: "lphrct"
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
