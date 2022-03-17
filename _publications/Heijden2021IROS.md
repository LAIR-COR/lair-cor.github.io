---
collection: publications
permalink: /conference/Heijden2021IROS
pubtype: conference
author: "van der Heijden, Bas and Ferranti, Laura and Kober, Jens and Babuska, Robert"
title: "DeepKoCo: Efficient Latent Planning with an Invariant Koopman Representation"
avenue: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)"
volume: 
number: 
pages: 183--189
year: 2021
bibtex: 
doi: "10.1109/IROS51168.2021.9636408"
file: "https://arxiv.org/pdf/2011.12690.pdf"
video: 
code: 
website: "https://arxiv.org/abs/2011.12690"
abstract: 
image: 
project: "opendr"
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
