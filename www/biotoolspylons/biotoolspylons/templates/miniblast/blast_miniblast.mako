<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1>Blast Results</h1>


<table border=1 class='blast-results'> 
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
   % if len(record.alignments) > 0:
   <tr> 
     <td colspan=3>
     <table> 
        <tr>
		<th>Title</th>
	    <th>Query</th>
	    <th>Query Length</th>
	    </tr>
	         
      % for alignment  in record.alignments: 
       <tr> 
         <td> ${alignment.title } </td>
         <td> ${alignment.length } </td>
         <td> ${len(alignment.hsps) } </td>
         <td> hsps.expect
         <td> hsps.score
         <td> hsps.query_start
         <td> hsps.query_end
       </tr>
     % endfor
     </table>     
	  </td>
      </tr>
     
   % endif
% endfor

</table> 
