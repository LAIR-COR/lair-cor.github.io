---
permalink: /
title: "LAIR: Learning, Autonomous, and Intelligent Robots"
excerpt: "LAIR:"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<br>
<p> Welcome to our webpage! We are are a part of Delft University of Technology, 3ME Faculty, Cognitive Robotics Group, Learning and Autononomous Control Group.</p>

<figure>
<img src="/images/group_photo.jpg" alt="Group Photo" style="width:100%"/>
<figcaption>A recent photo from the farewell party of Carlos, due to pandemic not all of us is present.</figcaption>
</figure>

### Recent News:
{% for news in site.news%}
   <ul>
   {% assign all_news = news.content | newline_to_br | split: '<br />' %} 
   {% for single in all_news limit:10 %}
   <li>   {{ single | remove: "</p>"}}
   {% endfor %}
{% endfor %}
   
