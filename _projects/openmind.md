---
title: "Robot-Assistance in Understanding and Educating Tooth Removal Procedures"
collection: projects
permalink: /projects/openmind
website: 
type: "NWO OpenMind; 2019"
logo: ../../../images/openmind.png
members: "Willem de Graaf (TUD), Tom van Riet (AMC), Dr.-Ing. Jens Kober (TUD)"
abstract: "<p> Though tooth removal is the most commonly performed surgical treatment worldwide, there has not been any real technological advancement in over 2000 years. There is still a lot of stress involved for patients, dental students, and (young) dentists. Up until now there is no scientific understanding of tooth removal procedures in terms of what motions and forces should be applied and this has its consequence on the quality of education. Students are highly undertrained when it comes tooth removal. The only way to prepare for a procedure is to read very limited instructions on ‘rocking and twisting’ motions and, in contrast to all other fields of dentistry, there is no way to practice these treatments pre-clinically. Practicing tooth removal therefore takes place on actual patients. </p>
<p> The goal of this project is to utilize modern robot technology to gain understanding of tooth extraction procedures and to use the acquired data to improve dental education. Bridging the scientific gap that exists in this field will have direct and significant clinical consequences and will lead to more confident dental students and dentists when practicing/performing these procedures, more efficient referral behavior and last but not least reduce discomfort and complication rates for the patient.</p>"
consortium: 
layout: archive
project: "openmind"
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

