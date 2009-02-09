from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234156664.574105
_template_filename='/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons/biotoolspylons/templates/fastas/created_fasta.mako'
_template_uri='/fastas/created_fasta.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n\n\n<h1>Uploaded New Fasta File. </h1>\n\n<p>\n')
        # SOURCE LINE 12
        __M_writer(unicode(h.rails.link_to("Return to Home Page", h.rails.url_for(action="index") ) ))
        __M_writer(u' | ')
        __M_writer(unicode(h.rails.link_to("Upload Another", h.rails.url_for(action="new") ) ))
        __M_writer(u' \n</p>\n\nSequences found in File: \n<table> \n\n')
        # SOURCE LINE 18
        for seq in c.sequences:
            # SOURCE LINE 19
            __M_writer(u'<tr><td>\n\t')
            # SOURCE LINE 20
            __M_writer(unicode(seq.description))
            __M_writer(u' \n</td></tr>\n')
        # SOURCE LINE 23
        __M_writer(u'\n<table> \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  <!-- add some head tags here -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


