---
title: "Deep Learning for Robust Robot Control (DL-foRCe)"
collection: projects
permalink: /projects/dlforce
website: 
type: "NWO Natural Artificial Intelligence; 2015-2019"
logo: 
members: "ir. Tim de Bruin__https://timdebruin.github.io/, Dr.-Ing. Jens Kober__http://www.jenskober.de, Prof Dr Sander Bohté__https://homepages.cwi.nl/~sbohte/, Prof Karl Tuyls__http://www.karltuyls.net/, prof.dr. Robert Babuška__http://www.robertbabuska.com/"
abstract: "<p> While robots can flawlessly execute a set of commands to achieve a task, these commands are mostly encoded by hand. There is a need for effective learning methods that can deal with the uncertainty in the robot's environment, in particular when only broad goals are specified, and the learning algorithm has to learn motor commands to achieve these goals. This typically involves reinforcement learning (RL). However, current RL for robotics tasks relies on ad hoc function approximators and is typically not robust to changes in the task, environment, or robot uncertainty (compliant robot actuators, or wear and tear). The aim of this project is to integrate two emerging notions in order to make reinforcement learning for robot control more robust and efficient: dynamic feedback control policies for robust control combined with deep neural networks to learn low-dimensional parameterizations of such control policies. This approach promises a generic and robust approach to reinforcement learning for robotic control. </p>"
consortium: 
layout: archive
project: "dl-force"
status: "completed"
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
{% assign pubs_by_date = site.publications | sort: "year" |  where: "project", page.project %}
{% for pub in pubs_by_date reversed %}
    {% include archive-single-pub.html %}
{% endfor %}

