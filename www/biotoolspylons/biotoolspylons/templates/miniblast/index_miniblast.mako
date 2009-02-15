<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1>Blast 2 files</h1>

<p>Select 2 file to blast</p>

${h.rails.form(h.rails.url(action='blast' ), method='POST',multipart=True)}
<%  flash_message = h.flash.pop_message()  %>
% if flash_message:
<div id="flash-message">${flash_message | h}</div>
% endif


Query File: ${ h.rails.select('fasta_filename1' , h.options_for_select( c.fasta_files ) )  } <br />
DB File: ${ h.rails.select('fasta_filename2' , h.options_for_select( c.fasta_files ) )  } <br />

${h.rails.submit('Submit')}<br />
</form>
${h.rails.end_form()}

