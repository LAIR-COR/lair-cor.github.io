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
       <div class="box">
           <img src="{{ person.image }}" alt="{{ person.title}}" style="width:200px;border-radius:50%" class="img-gallery" />
           <figcaption>{{ person.title}} </figcaption>
           <figcaption> {{person.contact}} </figcaption>
       </div>
       
    {% endfor %}
</div>

<h2> Researcher and Postdocs </h2>
    
<div class="photo-gallery">
    {% for person in site.researcher %}
       <div class="box">
           <img src="{{ person.image }}" alt="{{ person.title}}" style="width:200px;border-radius:50%" class="img-gallery" />
           <figcaption>{{ person.title}} </figcaption>
           <figcaption> {{person.contact}} </figcaption>
       </div>
       
    {% endfor %}
</div>


<h2> PhD Candidates </h2>
<div class="photo-gallery">
    {% for person in site.phd %}
       <div class="box">
           <img src="{{ person.image }}" alt="{{ person.title}}" style="width:200px;border-radius:50%" class="img-gallery" />
           <figcaption>{{ person.title}} </figcaption>
           <figcaption> {{person.contact}} </figcaption>
       </div>
       
    {% endfor %}
</div>


<!--
{% for person in site.prof reversed %}
  <h2>
    <figure>
    <img src="{{person.image}}" alt="person.title" style="width:200px"/>
    <figcaption>
        <a href="{{ person.weburl }}">
        {{ person.title }} - {{ person.contact }}
        </a>
    </figcaption>
    </figure>
  </h2>
{% endfor %}
-->
