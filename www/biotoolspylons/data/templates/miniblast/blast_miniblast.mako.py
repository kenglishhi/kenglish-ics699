from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234651275.3848391
_template_filename='/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons/biotoolspylons/templates/miniblast/blast_miniblast.mako'
_template_uri='/miniblast/blast_miniblast.mako'
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
        __M_writer(u'\n\n<h1>Blast Results</h1>\n\n\n<table border=1> \n    <tr> \n        <th>Database</th>\n\t    <th>Query</th>\n\t    <th>Query Length</th>\n    </tr> \n')
        # SOURCE LINE 16
        for record in c.blast_results:
            # SOURCE LINE 17
            __M_writer(u'    <tr> <td>')
            __M_writer(unicode(h.basename(record.database)))
            __M_writer(u'</td>\n         <td> ')
            # SOURCE LINE 18
            __M_writer(unicode(record.query))
            __M_writer(u' </td>\n         <td> ')
            # SOURCE LINE 19
            __M_writer(unicode(record.query_letters))
            __M_writer(u' </td>\n    </tr> \n    \n')
        # SOURCE LINE 23
        __M_writer(u'\n</table> \n')
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


