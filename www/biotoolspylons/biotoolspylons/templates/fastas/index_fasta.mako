<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1>University of Hawaii :: BioTools in Pylons</h1>
<ul>
<li> ${h.rails.link_to("Upload Fasta File", h.url_for(action="new") ) }
</ul>
Files: 
<ul>
% for item in c.fasta_files:
	<li> ${item} 
% endfor
</ul>



