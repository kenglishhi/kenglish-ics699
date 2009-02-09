<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>



<h1>My Controller</h1>

<p>Lorum ipsum dolor yadda yadda</p>

${h.rails.form(h.rails.url(action='upload'), multipart=True)}
Upload file: ${h.rails.file_field('uploadfile')} <br />
File description: ${h.rails.text_field('description')} <br />
${h.rails.submit('Submit')}<br /> 
</form>
${h.rails.end_form()}
