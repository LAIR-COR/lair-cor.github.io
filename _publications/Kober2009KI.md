---
collection: publications
permalink: /journal/Kober2009KI
pubtype: journal
author: "Kober, Jens and Peters, Jan"
title: "Reinforcement Learning fur Motor-Primitive"
avenue: "K\"unstliche Intelligenz"
volume: "9"
number: "3"
pages: 38--40
year: 2009
bibtex: 
doi: 
file: "http://www.jenskober.de/publications/Kober2009KI.pdf"
video: 
code: 
website: "https://web.archive.org/web/20180813193838/http://www.kuenstliche-intelligenz.de/archives/ki-journal-20160917/index.php-id=7779.html"
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
