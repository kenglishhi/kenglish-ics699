# -*- coding: utf-8 -*-
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <link href="/stylesheets/standard.css" media="screen" rel="stylesheet" type="text/css" /> 
    ${self.head_tags()}
    <title>BioTools in Pylons :: University of Hawaii </title>
  </head>
  <body>
  <div id="banner">
    <div id="banner-message">
       <ul id="secondary-nav">
          Bio Tools with Pylons | ${h.rails.link_to("Fasta Files", h.rails.url_for(controller='fastas', action="index") ) }  |
                ${h.rails.link_to("Upload Fasta File", h.rails.url_for(controller='fastas', action="new") ) }  
            <br/>
    <span>
       <a href="/notifications"><span id="notifications_monitor"> 
</span></a> 
    </span>       
    
</ul>

        </div>
          
        
    </div>

    ${self.body()}
  </body>
</html>

