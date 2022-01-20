---
layout: archive
title: "Thesis"
permalink: /thesis/
author_profile: false
---
{% include base_path %}


<h2> Internships / research assistantships </h2>

<p> Our department does not offer any such positions for external BSc or MSc students. </p>

<h2> BSc projects </h2>

<p> See BrightSpace for Bachelor End Projects for TU Delft students. Only in rare exceptions, we can accommodate external students (and they definitely need to be self-funded, e.g. via Erasmus+). </p>


<h2> MSc projects </h2>

<p> See BrightSpace for Bachelor End Projects for TU Delft students. Only in rare exceptions, we can accommodate external students (and they definitely need to be self-funded, e.g. via Erasmus+). </p>


<h2> BSc projects </h2>

<p> Vacancies for projects again from Q2 22/23 onwards. I will be able to accept a few TU Delft students of the MSc Robotics, of the Vehicle Engineering track and BioRobotics as well as Haptics Interfaces specialization within the MSc Mechanical Engineering (see BrightSpace for project descriptions). For all other TU Delft MSc programs, tracks, and specializations see below. Only in rare exceptions, we can accommodate external students (and they definitely need to be self-funded, e.g. via Erasmus+). </p>

<h2> Initiative Applications </h2>

<p>We can occasionally accommodate (additional) highly motivated students in MSc projects or in ongoing projects before their graduation stage.</p>

<p>If you are interested in working on a project with us, please send us ca. 1 academic quarter before the intended starting date an e-mail including:</p>

*  a short CV (½ - 1 page
*  BSc &amp; MSc transcripts
*  a short motivation letter
*  BSc thesis (PDF)
*  any other information that might be relevant for the application

<p>The motivation letter should state</p>

*  what you are interested in (control/ML topic and/or application)
*  the type of assignment you are interested in (more theoretical/more applied)
*  whether you prefer a project at the TU or at a company
*  the intended starting date
*  your relevant experience (studies, technical projects, internships, hobbies, etc.)
*  programming languages and related (Python, C, C++, ROS, etc.)

<h2> Ongoing Thesis </h2>
{% for thesis in site.ongoing_thesis %}
  *  **{{ thesis.student }}**  Mentor(s): {{ thesis.mentors }}  <br> *"{{ thesis.topic }}"*
{% endfor %}

<h2> Completed Thesis </h2>

{% for thesis in site.completed_thesis %}
   {% assign thesis_entries = thesis.content | newline_to_br | split: '<br />' %}
   <ul>
   {% for thesis_entry in thesis_entries %}
        {{thesis_entry}}
        
   {% endfor %}
   </ul>
{% endfor %}
