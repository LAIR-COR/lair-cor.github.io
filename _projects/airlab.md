---
title: "AI for Retail (AIR) Lab Delft"
collection: projects
permalink: /projects/airlab
website: https://aiforretail.ai/
type: "Industry project (Ahold Delhaize); 2019-2022"
logo: ../../../images/airlab.jpg
members: "ir. Mert Imre, ir. Maximilian Kronmüller, ir. Corrado Pezzato, ir. Max Spahn, Madelaine Ley, dr. Filippo Santoni de Sio, dr. ir. Carlos Hernández Corbato, dr. Javier Alonso-Mora, Dr.-Ing. Jens Kober, prof.dr.ir. Martijn Wisse"
abstract: "<p> The AI for Retail (AIR) Lab Delft is a joint TUDelft-Ahold Delhaize industry lab consisting of a robotics research program and test site focused on developing state-of-the-art innovations in the retail industry. By expanding its focus to robotics, AIRLab Delft will further drive innovations for daily business while building more knowledge of the intersection between retail, AI and robotics. The expansion comprises a robotics research program and test site for developing state-of-the-art innovations in the retail industry. </p>
<p>Based in RoboValley, a robotics research center developed by TU Delft Robotics Institute, a team of international researchers will explore robotic solutions that can be applied throughout the retail supply chain, from warehouses and stores to customers. To ensure these explorations result in tangible solutions, Ahold Delhaize will open a test site where researchers can work with partners, students and start-ups, supported by the technology incubator of TU Delft – YES!Delft – to build and test prototypes of robotic solutions. At the test site, which will be operational in early 2019, they will explore how robotics can be deployed in a retail setting, how robotic grippers can handle delicate items such as fruits and vegetables, or how to improve image-recognition of products and packaging.</p>"
consortium: 
layout: archive
project: "airlab"
status: "ongoing"
---
{% include base_path %}

{% if page.logo %}
<p align="center">
{% if page.website %}
<a href="{{ page.website }}"> <img src="{{  page.logo }}" alt="Logo skipped" style="max-height:200px"/> </a>
{% else %}
<img src="{{  page.logo }}" alt="Logo skipped" />
{% endif %}
</p>
{% endif %}

<p> <strong> <em> Abstract: </em> </strong> {{ page.abstract }}
    {% if page.webpage %}
        <a href="{{ page.website}}"> <br> More information </a>
    {% endif %}
</p>

<p> <strong> Project Type: </strong> {{ page.type }}</p>

{% if page.consortium  %}
<p> <strong> Consortium: </strong>
{% assign members = page.consortium | split: ", " %}
{% for member in members %}
{% if member contains "__" %}
{% assign memberWithLink  = member | split: "__" %}
{% if member != members.last %}
<a href="{{ memberWithLink.last }}">{{ memberWithLink.first }} </a>,
{% else %}    
<a href="{{ memberWithLink.last }}">{{ memberWithLink.first }} </a>
{% endif %}
{% else %}
{% if member != members.last %}
{{ member }},
{% else %}    
{{ member }}
{% endif %}
{% endif %}
{% endfor %}
{% endif  %}

<p> <strong> Members: </strong>  
{% assign members = page.members | split: ", " %}
{% assign pubs_by_date = site.publications | sort: "year"%}

{% for member in members %}
{% if member contains "__" %}
{% assign memberWithLink  = member | split: "__" %}
{% if member != members.last %}
<a href="{{ memberWithLink.last }}">{{ memberWithLink.first }} </a>,
{% else %}    
<a href="{{ memberWithLink.last }}">{{ memberWithLink.first }} </a>
{% endif %}
{% else %}
{% if member != members.last %}
{{ member }},
{% else %}    
{{ member }}
{% endif %}
{% endif %}
{% endfor %}
</p>

<h2> Publications </h2>

{% for post in pubs_by_date reversed %}
{% if post.project contains page.project %}
{% include archive-single-pub.html %}
{% endif %}
{% endfor %}
