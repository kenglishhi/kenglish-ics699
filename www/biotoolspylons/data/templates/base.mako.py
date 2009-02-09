from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234152126.4347751
_template_filename=u'/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons/biotoolspylons/templates/base.mako'
_template_uri=u'/fastas/../base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n    <link href="/stylesheets/standard.css" media="screen" rel="stylesheet" type="text/css" /> \n    ')
        # SOURCE LINE 7
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n    <title>BioTools in Pylons :: University of Hawaii </title>\n  </head>\n  <body>\n  <div id="banner">\n    <div id="banner-message">\n       <ul id="secondary-nav">\n          Bio Tools with Pylons | ')
        # SOURCE LINE 14
        __M_writer(unicode(h.rails.link_to("Fasta Files", h.rails.url_for(controller='fastas', action="index") ) ))
        __M_writer(u'  |\n                ')
        # SOURCE LINE 15
        __M_writer(unicode(h.rails.link_to("Upload Fasta File", h.rails.url_for(controller='fastas', action="new") ) ))
        __M_writer(u'  \n            <br/>\n    <span>\n       <a href="/notifications"><span id="notifications_monitor"> \n</span></a> \n    </span>       \n    \n</ul>\n\n        </div>\n          \n        \n    </div>\n\n    ')
        # SOURCE LINE 29
        __M_writer(unicode(self.body()))
        __M_writer(u'\n  </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


