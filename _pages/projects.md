---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: false
---
{% include base_path %}


{% for project in site.projects reversed%}
   <h2> {{ project.name }} Projects</h2>
   
   {% assign entry = project.content | newline_to_br | split: '<br />' %}
   {% for e in entry %}
   <li>   {{ e | strip_html }} 
   {% endfor %} 
   
   
{% endfor %}

