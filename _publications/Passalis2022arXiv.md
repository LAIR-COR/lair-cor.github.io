---
collection: publications
permalink: /preprint/Passalis2022arXiv
pubtype: preprint
author: "Passalis, Nikolaos and Pedrazzi, Stefania and Babuska, Robert and Burgard, Wolfram and Dias, Daniel and Ferro, Francesco and Gabbouj, Moncef and Ole, Green and Iosifidis, Alexandros and Kayacan, Erdal and Kober, Jens and Michel, Olivier and Nikolaidis, Nikolaos and Nousi, Paraskevi and Pieters, Roel S. and Tzelepi, Maria and Valada, Abhinav and Tefas, Anastasios"
title: "OpenDR: An Open Toolkit for Enabling High Performance, Low Footprint Deep Learning for Robotics"
avenue: 
volume: 
number: 
pages: 
year: 2022
bibtex: 
doi: 
file: "https://arxiv.org/pdf/2203.00403.pdf"
video: 
code: 
website: "https://arxiv.org/abs/2203.00403"
abstract: 
image: 
project: "opendr"
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