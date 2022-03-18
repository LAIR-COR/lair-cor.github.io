---
title: "Cognitive Robots for Flexible Agro Food Technology (FlexCRAFT)"
collection: projects
permalink: /projects/flexcraft
website: https://flexcraftprogram.com/
type: "NWO Perspectief; 2019-2022"
logo: ../../../images/flexcraft.png
members: "ir. Padmaja Kulkarni__https://www.tudelft.nl/en/3me/departments/cognitive-robotics-cor/people/, ir. Rodrigo J. Pérez-Dattari__https://www.tudelft.nl/staff/s.p.mulders/, Dr.-Ing. Jens Kober__http://www.jenskober.de, prof.dr. Robert Babuška__http://www.robertbabuska.com/"
abstract: "<p> Food production must be as hygienic, efficient and sustainable as possible. Furthermore, fewer people are willing to do tedious and heavy work in warm greenhouses or in refrigerated rooms where chicken products are processed, for example. Robots can provide a solution to this problem if they can deal with the considerable variations in shape, size and hardness of different food products. This is still challenging. The programme FlexCRAFT will develop new robot technology for such purposes as the automatic harvesting of tomatoes, for example. The robotics developed must also help with the processing of foodstuffs. Examples of this include the processing and packaging of chicken products, but also neatly packaging bags of crisps and packets of biscuits in boxes of varying sizes. </p>
<p>The Netherlands is the second biggest exporter of agro-food products worldwide and the third biggest supplier of technology for the agro-food sector. This programme will contribute to strengthening the competitive position of the Netherlands in these sectors. </p>"
consortium: "3DUniversum, ABB, AgriFoodTech Platform, Aris BV, BluePrint Automation, Cellar Land, Cerescon, Delft University of Technology, Demcon, Eindhoven University of Technology, Festo, GMV, Houdijk Holland, Marel Stork Poultry Processing, Maxon Motor, Priva, Protonic Holland, Rijk Zwaan, University of Amsterdam, University of Twente, Wageningen University & Research"
layout: archive
project: "flexcraft"
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

