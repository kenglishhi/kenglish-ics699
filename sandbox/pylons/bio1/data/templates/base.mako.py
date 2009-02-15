from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234140498.1826749
_template_filename=u'/home/kenglish/sandbox/pylons/bio1/bio1/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n    <link href="/stylesheets/standard.css" media="screen" rel="stylesheet" type="text/css" /> \n    ')
        # SOURCE LINE 7
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n    <title>Asia-Pacific Web BioTools</title>\n  </head>\n  <body>\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(self.body()))
        __M_writer(u'\n  </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


