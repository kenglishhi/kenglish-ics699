<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1>Blast Results</h1>


<table border=1> 
    <tr> 
        <th>Database</th>
	    <th>Query</th>
	    <th>Query Length</th>
    </tr> 
% for record in c.blast_results:
    <tr> <td>${h.basename(record.database)}</td>
         <td> ${record.query} </td>
         <td> ${record.query_letters} </td>
    </tr> 
    
% endfor

</table> 
