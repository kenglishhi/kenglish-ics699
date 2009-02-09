<%inherit file="../base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>



<h1>My Controller</h1>

<p>Select a file from your filesystem to upload</p>

${h.rails.form(h.rails.url(action='create' ), method='POST',multipart=True)}
Upload file: ${h.rails.file_field('uploadfile')} <br />
${h.rails.submit('Submit')}<br /> 
</form>
${h.rails.end_form()}
