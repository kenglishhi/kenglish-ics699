<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>



<h1>Home Page </h1>
<ul>
<li>${h.rails.link_to("Upload Fasta File", h.rails.url_for(controller="bio",action="form") ) }
</ul>
Files: 
<ul>
% for item in c.fasta_files:
	${item} <br />
% endfor
</ul>


<p>Lorum ipsum dolor yadda yadda</p>

