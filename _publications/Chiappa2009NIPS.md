---
collection: publications
permalink: /conference/Chiappa2009NIPS
pubtype: conference
author: "Chiappa, Silvia and Kober, Jens and Peters, Jan"
title: "Using Bayesian Dynamical Systems for Motion Template Libraries"
avenue: "Advances in Neural Information Processing Systems 21 (NIPS 2008)"
volume: 
number: 
pages: 297--304
year: 2009
bibtex: 
doi: 
file: "http://papers.nips.cc/paper/3429-using-bayesian-dynamical-systems-for-motion-template-libraries.pdf"
video: "https://youtu.be/09QwdoDuMTc"
code: 
website: "http://papers.nips.cc/paper/3429-using-bayesian-dynamical-systems-for-motion-template-libraries"
abstract: 
image: 
project: 
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