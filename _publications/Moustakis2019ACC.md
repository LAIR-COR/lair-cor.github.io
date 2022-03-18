---
collection: publications
permalink: /conference/Moustakis2019ACC
pubtype: conference
author: "Moustakis, Nikolaos and Mulders, Sebastiaan Paul and Kober, Jens and van Wingerden, Jan-Willem"
title: "A Practical Bayesian Optimization Approach for the Optimal Estimation of the Rotor Effective Wind Speed"
avenue: "American Control Conference (ACC)"
volume: 
number: 
pages: 4179--4185
year: 2019
bibtex: 
doi: "10.23919/ACC.2019.8814622"
file: "http://www.jenskober.de/publications/Moustakis2019ACC.pdf"
video: 
code: 
website: 
abstract: 
image: 
project: "wtbrain"
---
{% include base_path %}

{% if page.image %}
<p align="center">
{% if page.website %}
<a href="{{ page.website }}"> <img src="{{  page.image }}" alt="Paper Image not loaded." style="max-height:400px;max-width:400px"/> </a>
{% else %}
<img src="{{  page.image }}" alt="Paper Image not loaded." />
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


{% if page.video and page.video contains "embed" %}
<h2> Video </h2>
<div align="center">
<iframe width="420" height="315" src="{{ page.video }}" frameborder="0" allowfullscreen ></iframe>
</div>
{% endif %}


<div align="center" style="margin-top: 50px">
{% if page.doi %}
<button name="button" onclick="{{ page.doi }}" style="height:40px;width:100px">DOI</button>
{% endif %}
{% if page.file %}
<button name="button" onclick="{{ page.file }}" style="height:40px;width:100px">PDF</button>
{% endif %}
{% if page.video %}
<button name="button" onclick="{{ page.video }}" style="height:40px;width:100px">Video</button>
{% endif %}
{% if page.code %}
<button name="button" onclick="{{ page.code }}" style="height:40px;width:100px">Code</button>
{% endif %}
{% if page.website %}
<button name="button" onclick="{{ page.website }}" style="height:40px;width:100px">Site</button>
{% endif %}
</div>