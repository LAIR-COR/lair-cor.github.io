---
title: "Open Deep Learning Toolkit for Robotics (OpenDR)"
collection: projects_ongoing
permalink: /projects/ongoing/opendr
website: https://opendr.eu/
type: "EU Horizon 2020 program, call H2020-ICT-2018-2020 (Information and Communication Technologies); 2019 – 2022"
logo: ../../../images/opendr.png
members: "ir. Bas van der Heijden, Dr. Osama Mazhar, Dr. Laura Ferranti__http://lauraferranti.com/, Dr.-Ing. Jens Kober__http://www.jenskober.de, prof.dr. Robert Babuška__http://www.robertbabuska.com/"
abstract: "The aim of OpenDR is to develop a modular, open and non-proprietary deep learning toolkit for robotics. We will provide a set of software functions, packages and utilities to help roboticists develop and test robotic applications that incorporate deep learning. OpenDR will enable linking robotics applications to software libraries such as tensorflow and the ROS operating environment. We focus on the AI and cognition core technology in order to give robotic systems the ability to interact with people and environments by means of deep-learning methods for active perception, cognition and decisions making. OpenDR will enlarge the range of robotics applications making use of deep learning, which will be demonstrated in the applications areas of healthcare, agri-food and agile production."
consortium: "Aristotle University of Thessaloniki, Tampere University of Technology, Aarhus University, Delft University of Technology, Albert-Ludwigs-Universität Freiburg, Cyberbotics Ltd., PAL Robotics S.L., Agro Intelligence ApS"
layout: archive
project: "opendr"
---
{% include base_path %}

{% if page.logo %}
<p align="center">
<a href="{{ page.website }}"> <img src="{{  page.logo }}" alt="Logo skipped" /> </a>
{% endif %}
</p>

<p> <strong> <em> Abstract: </em> </strong> {{ page.abstract }} <a href="{{ page.website}}"> More information </a></p>
<p> <strong> Project Type: </strong> {{ page.type }}</p>
<p> <strong> Consortium: </strong> {{ page.consortium }}</p>
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
{% assign conferences_by_date = site.conference | sort: "year" |  where: "project", page.project %}
{% for c in conferences_by_date reversed %}
* {{ c.author }}, [**{{ c.title }}**]({{c.permalink}}), *{{ c.avenue}}*, {{c.year}}  {%unless c.video=="" or c.video == null%}  [video]({{c.video}}) {%    endunless %}
{% endfor %}



