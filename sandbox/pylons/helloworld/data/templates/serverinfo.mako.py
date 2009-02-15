from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1233810488.3592091
_template_filename='/home/kenglish/sandbox/pylons/helloworld/helloworld/templates/serverinfo.mako'
_template_uri='/serverinfo.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<h2>\nServer info for ')
        # SOURCE LINE 2
        __M_writer(unicode(request.host))
        __M_writer(u'\n</h2>\n\n<p>\nThe URL you called: ')
        # SOURCE LINE 6
        __M_writer(unicode(h.rails.url_for()))
        __M_writer(u'\n</p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


