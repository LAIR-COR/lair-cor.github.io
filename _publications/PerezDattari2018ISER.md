---
collection: publications
permalink: /conference/PerezDattari2018ISER
pubtype: conference
author: "Perez-Dattari, Rodrigo and Celemin, Carlos E. and Ruiz-del-Solar, Javier and Kober, Jens"
title: "Interactive Learning with Corrective Feedback for Policies based on Deep Neural Networks"
avenue: "International Symposium on Experimental Robotics (ISER)"
volume: 
number: 
pages: 353--363
year: 2018
bibtex: 
doi: "10.1007/978-3-030-33950-0_31"
file: "http://www.jenskober.de/publications/PerezDattari2018ISER.pdf"
video: "https://youtu.be/vcEtuRrRIe4"
code: "https://github.com/rperezdattari/Interactive-Learning-with-Corrective-Feedback-for-Policies-based-on-Deep-Neural-Networks"
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
