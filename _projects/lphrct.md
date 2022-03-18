---
title: "Learning Physical Human-Robot Cooperation Tasks"
collection: projects
permalink: /projects/lphrct
website: 
type: "Industry project (Honda Research Institute Europe GmbH, HTSM PPS-toeslag); 2017-2021"
logo: ../../../images/lphrct.png
members: "ir. Linda van der Spaa__https://www.tudelft.nl/staff/l.f.vanderspaa/, Dr. Jihong Zhu__https://jihong-zhu.github.io/, Dr.-Ing. Jens Kober__http://www.jenskober.de, Dr.-Ing. Michael Gienger__https://www.honda-ri.de/people/"
abstract: "<p> Human-robot interaction and collaboration is of fundamental importance for any robot leaving the safety of fences on a highly-structured factory floor: service and care scenarios, medical applications, offshore, maintenance and inspection, as well as industrial assembly. In this project, we will develop new concepts and techniques for robot learning that endow robots with the capability to physically interact and collaborate with humans. In particular, we will consider tasks related to joint handling of large objects, i.e., jointly transporting and manipulating them. Examples include transporting and assembling light traverses, or changing tires on a car. </p>"
consortium: 
layout: archive
project: "lphrct"
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
