<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1>Blast Results</h1>


<ul> 
% for record in c.results:
    <li> ${record.query}
% endfor

</ul> 
