---
collection: publications
permalink: /journal/Chen2020TMECH
pubtype: journal
author: "Chen, X. and Tan, X. and Berselli, G. and Chen, X. and Clayton, G. and Jeon, S. and Karimi, H. R. and Katsura, S. and Kober, J. and Lan, C.-C. and Leonessa, A. and Li, Z. and Liu, G. and Oetomo, D. and Oldham, K. and Pan, Y.-J. and Shimono, T. and Sun, T. and Tavakoli, M. and Ueda, J. and Vallery, H. and Xu, Q. and Yi, J. and Zhang, L. and Zuo, L."
title: "Guest Editorial: Focused Section on Inaugural Edition of TMECH/AIM Emerging Topics"
avenue: "IEEE/ASME Transactions on Mechatronics"
volume: "25"
number: "4"
pages: 1695-1697
year: 2020
bibtex: 
doi: "10.1109/TMECH.2020.3000228"
file: "https://ieeexplore.ieee.org/document/9166906"
video: 
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