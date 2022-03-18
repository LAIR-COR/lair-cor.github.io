---
title: "Teaching Robots Interactively (TERI)"
collection: projects
permalink: /projects/teri
website: 
type: "ERC Starting Grant; 2019-2023"
logo: 
members: "dr. Zlatan Ajanović__https://www.zlatanajanovic.com/, dr. Carlos E. Celemin Paez__https://sites.google.com/view/carloscelemin, dr. Marta Ferraz__https://nl.linkedin.com/in/marta-ferraz-a6200551, ing. Giovanni Franzese__https://nl.linkedin.com/in/giovanni-franzese-6a7318168, Dr.-Ing. Jens Kober__http://www.jenskober.de, dr. Ravi Prakash__https://in.linkedin.com/in/ravi-prakash-a93ab9a8, dr. Leandro de Souza Rosa__https://it.linkedin.com/in/lsr/en-us"
abstract: "<p> Programming and re-programming robots is extremely time-consuming and expensive, which presents a major bottleneck for new industrial, agricultural, care, and household robot applications. My goal is to realize a scientific breakthrough in enabling robots to learn how to perform manipulation tasks from few human demonstrations, based on novel interactive machine learning techniques. </p>
<p>Current robot learning approaches focus either on imitation learning (mimicking the teacher’s movement) or on reinforcement learning (self-improvement by trial and error). Learning even moderately complex tasks in this way still requires infeasibly many iterations or task-specific prior knowledge that needs to be programmed in the robot. To render robot learning fast, effective, and efficient, I propose to incorporate intermittent robot-teacher interaction, which so far has been largely ignored in robot learning although it is a prominent feature in human learning. This project will deliver a completely new and better approach: robot learning will no longer rely on initial demonstrations only, but it will effectively use additional user feedback to continuously optimize the task performance. It will enable the user to directly perceive and correct undesirable behavior and to quickly guide the robot toward the target behavior. In my previous research I have made ground-breaking contributions to the existing learning paradigms and I am therefore ideally prepared to tackle the three-fold challenge of this project: developing theoretically sound techniques which are at the same time intuitive for the user and efficient for real-world applications.</p>
<p>The novel framework will be validated with generic real-world robotic force-interaction tasks related to handling and (dis)assembly. The potential of the newly developed teaching framework will be demonstrated with challenging bi-manual tasks and a final study evaluating how well novice human operators can teach novel tasks to a robot.</p>"
consortium: 
layout: archive
project: "teri"
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

