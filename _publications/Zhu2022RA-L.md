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
video: "https://youtube.com/embed/yY4k1nnhA60"
code: "https://github.com/Jihong-Zhu/learning-tp-skills-from-few-demos"
website: "https://sites.google.com/view/tp-gmm-from-few-demos/"
abstract: "Moving away from repetitive tasks, robots nowadays demand versatile skills that adapt to different situations. Task-parameterized learning improves the generalization of motion policies by encoding relevant contextual information in the task parameters, hence enabling flexible task executions. However, training such a policy often requires collecting multiple demonstrations in different situations. To comprehensively create different situations is non-trivial thus renders the method less applicable to real-world problems. Therefore, training with fewer demonstrations/situations is desirable. This paper presents a novel concept to augment the original training dataset with synthetic data for policy improvements, thus allows learning task-parameterized skills with few demonstrations. "
image: ../../../paper_images/Zhu2022RA-L.png
project: "lphrct"
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
<button name="button" onclick="window.location.href='{{ page.doi }}'" style="height:40px;width:100px">DOI</button>
{% endif %}
{% if page.file %}
<button name="button" onclick="window.location.href='{{ page.file }}'" style="height:40px;width:100px">PDF</button>
{% endif %}
{% if page.video %}
<button name="button" onclick="window.location.href='{{ page.video }}'" style="height:40px;width:100px">Video</button>
{% endif %}
{% if page.code %}
<button name="button" onclick="window.location.href='{{ page.code }}'" style="height:40px;width:100px">Code</button>
{% endif %}
{% if page.website %}
<button name="button" onclick="window.location.href='{{ page.website }}'" style="height:40px;width:100px">Site</button>
{% endif %}
</div>
