---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---
{% include base_path %}

<h2> Journal Papers </h2>

{% assign journals_by_date = site.journal | sort: "year" %}
{% for j in journals_by_date reversed %}
  * {{ j.author }}, [**{{ j.title }}**]({{j.permalink}}), *{{ j.avenue}}*, {{j.year}} 
{% endfor %}

<h2> Conference Papers </h2>
{% assign conferences_by_date = site.conference | sort: "year" %}
{% for c in conferences_by_date reversed %}
  * {{ c.author }}, [**{{ c.title }}**]({{c.permalink}}), *{{ c.avenue}}*, {{c.year}} 
{% endfor %}


<h2> Preprints </h2>
{% assign preprints_by_date = site.preprints | sort: "year" %}
{% for p in preprints_by_date reversed %}
  * {{ p.author }}, [**{{ p.title }}**]({{p.permalink}}), {{p.year}} 
{% endfor %}


<h2> Books, Chapters, and Others </h2>
{% assign others_by_date = site.others | sort: "year" %}
{% for o in others_by_date reversed %}
  * {{ o.author }}, [**{{ o.title }}**]({{o.permalink}}), {{o.year}} 
{% endfor %}

<!--
{% for post in site.journal %}
    {% include archive-single.html %} 
{% endfor %}
-->
