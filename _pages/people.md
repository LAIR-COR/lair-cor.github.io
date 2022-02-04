---
layout: archive
title: "People"
permalink: /people/
author_profile: false
---
{% include base_path %}



<h2> Head </h2>

<div class="photo-gallery">
    {% for person in site.prof %}
           <a href="{{ person.permalink }}"> <img src="{{ person.image }}" alt="{{ person.title}}" style="width:300px;border-radius:50%" class="img-gallery"/> </a>
       
    {% endfor %}
</div>

<h2> Researchers and Postdocs </h2>
    
<div class="photo-gallery">
    {% for person in site.researcher %}
           <img src="{{ person.image }}" alt="{{ person.title}}" style="width:240px;border-radius:50%;margin:20px" class="img-gallery" />
               
    {% endfor %}
</div>


<h2> PhD Candidates </h2>
<div class="gallery">

    {% for person in site.phd %}
           <a href="{{ person.permalink }}"> <img src="{{ person.image }}" alt="{{ person.title}}" style="width:240px;border-radius:50%;margin:10px" class="img-gallery" /> </a>
    {% endfor %}  
</div>


