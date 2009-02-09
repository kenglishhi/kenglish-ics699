<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>



<h1>Uploaded New Fasta File. </h1>

<p>
${h.rails.link_to("Return to Home Page", h.rails.url_for(action="index") ) } | ${h.rails.link_to("Upload Another", h.rails.url_for(action="new") ) } 
</p>

Sequences found in File: 
<table> 

% for seq in c.sequences:
<tr><td>
	${seq.description} 
</td></tr>
% endfor

<table> 

