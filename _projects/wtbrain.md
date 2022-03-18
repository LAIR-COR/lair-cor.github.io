---
title: "Wind Turbine Brain (WT Brain)"
collection: projects
permalink: /projects/wtbrain
website: 
type: "TKI Wind op Zee; 2017-2020"
logo: ../../../images/wtbrain.png
members: "ir. Sebastiaan P. Mulders__https://www.tudelft.nl/staff/s.p.mulders/ Dr.-Ing. Jens Kober__www.jenskober.de, prof.dr.ir. Jan-Willem van Wingerden__https://www.tudelft.nl/en/3me/departments/delft-center-for-systems-and-control/people/professors/profdrir-jw-van-wingerden-jan-willem/"
abstract: "<p> <strong> Background </strong> Wind turbines behave well in a lot of different wind conditions, in the lightest breeze and the heaviest storms. In the end, it boils down to producing energy at the lowest possible cost. That is why the system that controls the response of a wind turbine to the wind, must keep finding a balance between producing energy and the loads acting on the wind turbine. This project focusses on finding new ways to finding this balance. These new ways are becoming available due to the rapid scientific progress in the fields of (deep) machine learning and the use of, amongst other things, neural networks. By applying these methods in wind turbine control, we expect to realise a 5-10% design equivalent load reduction.</p>
<p> <strong>Goal/ objective </strong> The goal of the project is to improve the wind turbine controller and its design process. This will be achieved by using machine learning (ML) to tune the controller in the design phase. The controller will contain conventional estimators and controller structures. Neural or Bayesian networks (hereafter: artificial networks (AN)) will be used to search for opportunities to further improve the conventional controller design.</p>
<strong>Work programme</strong>
<ol>
    <li> ML methods and AN architectures: AN types are compared and the architecture of an AN-based controller is selected. Based on that selection, appropriate ML methods are selected.</li>
    <li> Conventional controller tuning with ML: The selected target function may be difficult to capture for the conventional controller. ML can tune the parameters based on the target function directly.</li>
    <li> AN-controller: Incorporate AN in the controller and tune it.</li>
    <li> Tuning and testing: The new controller structures are tuned for manufacturer and theoretical wind turbine models </li>
</ol>

<p><strong>Outcome:</strong> Situations where improvements are sought are low, normal and highly turbulent winds, starts and stops and extreme wind conditions, such as extreme operating gusts or extreme direction changes. The improvement is expected to reduce design equivalent loads on the blades and the wind turbine tower and to reduce extreme loads. These reductions can directly reduce the cost of a wind turbine. Alternatively, the load reduction on the blades can be used to employ longer blades, resulting in a higher production.<p>"
consortium: Energy Research Centre of the Netherlands (ECN)__https://www.ecn.nl/, Lagerwey Group B.V.__https://www.lagerwey.com/, TU Delft__https://www.tudelft.nl/en/, Siemens Gamesa__https://www.siemensgamesa.com/en-int
layout: archive
project: "wtbrain"
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
