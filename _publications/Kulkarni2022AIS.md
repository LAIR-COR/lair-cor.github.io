---
collection: publications
permalink: /journal/Kulkarni2022AIS
pubtype: journal
author: "Kulkarni, Padmaja and Kober, Jens and Babuska, Robert and Della Santina, Cosimo"
title: "Learning Assembly Tasks in a Few Minutes by Combining Impedance Control and Residual Recurrent Reinforcement Learning"
avenue: "Advanced Intelligent Systems"
volume: "4"
number: "1"
pages: 2100095
year: 2022
bibtex: 
doi: "10.1002/aisy.202100095"
file: "https://onlinelibrary.wiley.com/doi/pdf/10.1002/aisy.202100095"
video: "https://www.authorea.com/doi/full/10.22541/au.162671181.19429485"
code: 
website: 
abstract: 
image: 
project: "flexcraft"
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
