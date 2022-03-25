How to add content?

1) News
You will need to update the recent.md file located inside _news folder. You need to add recent news on top of the other news. The page will automatically show ten news that are on top of the stack.
Do not change the header part. (The part between '---' ) You can use general markdown styling for using links or textstyling.
 
2) People

2.1) Adding new people
You need to add a new file to _people page, preferably firstname.md. You can check other files in that folder to see how to fill. An example is below. An empty template is in draft folder named, person.md. Permalink should be role/name ie phd

 If you have a photo of the person, add it to the images folder, preferably named as firstname, format can be jpeg or png. (The image is better if it is square). I did not add content information to the pages as a text, rather embed it on the images. The script used for creating those stamped images, and the font can be found in custom_scripts folder. To be able to generate stamped image you need PIL and python 3.  
---
title: "Ravi Prakash"
collection: people
role: researcher
permalink: /people/ravi
weburl: 'https://www.tudelft.nl/en/staff/r.prakash-1/'
image: /images/ravi.jpg
stamped_image: /images/ravi_stamped.png
contact: R.Prakash-1_AT_tudelft.nl
---

2.2) Changing your own page.
You can change personal content by finding your file in _people folder. You need to keep the header (the part between "---"s). You can edit below that. You can use HTML, CSS and Javascript to customize your own page.
/rodrigo

3) Publications 
3.1) Adding a new publication
You need to add a file to _publication folder. You can use the bibtex to fill most of the information. The easiest way to start would be to copy and paste publication.md file from drafts folder and fill the header with required information. Most information on the header should be between quotation marks, so make sure to use them. You can check already existing files' headers to be sure. If some parts of the header is not applicable for your work, leave it blank. Permalink should be publicationType/shortcut ie /conference/Bruin2015NIPS_WS

3.2) Page for the publication
If you want to customize the page of the publication, you can update the part below the header. You can use HTML, CSS and JS to create a detailed page for the publication. I created one for Jihong's work. You can examine: Zhu2022RA-L.md

Note: if you want to add an image for the paper, you can use paper_images folder.


4) Thesis
4.1) Adding a new ongoing thesis
You need to add a file tho the _thesis folder. An empty template is in drafts folder with name thesis.md, you can copy and paste that file into _thesis folder and rename it. The naming is lastname.md so far. You can check other ongoing thesis to see how to fill information.

4.2) Turning an ongoing thesis into completed thesis
Find the thesis file in _thesis folder. Change status in the header from ongoing to completed. If you have the link of the thesis from the university repository, add it to urllink in header, which should initially be blank.


5) Adding a new project
The easiest way would be to copy paste an existing project file and adapt it to the new project.

6) More than that
If you want to change things beyond individual pages, then you may need to update different files. If you are planning to make bigger changes, I would suggest you to install the required packages locally, and make changes and test locally until you make it look the way you want. https://github.com/academicpages/academicpages.github.io explains how
