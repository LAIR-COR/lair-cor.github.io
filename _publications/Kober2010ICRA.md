---
collection: publications
permalink: /conference/Kober2010ICRA
pubtype: conference
author: "Kober, Jens and Muelling, Katharina and Kroemer, Oliver and Lampert, Christoph H. and Scholkopf, Bernhard and Peters, Jan"
title: "Movement Templates for Learning of Hitting and Batting"
avenue: "IEEE International Conference on Robotics and Automation (ICRA)"
volume: 
number: 
pages: 69--82
year: 2010
bibtex: 
doi: "10.1109/robot.2010.5509672"
file: "http://www.ias.informatik.tu-darmstadt.de/publications/ICRA2010-Kober_6231[1].pdf"
video: "https://youtu.be/SsvKbOt4L8M"
code: "http://jenskober.de/code.php"
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
