from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234917947.152178
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
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u"\n\n<h1>Blast Results</h1>\n\n\n<table border=1 class='blast-results'> \n    <tr> \n        <th>Database</th>\n\t    <th>Query</th>\n\t    <th>Query Length</th>\n    </tr> \n")
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
            __M_writer(u' </td>\n    </tr> \n')
            # SOURCE LINE 21
            if len(record.alignments) > 0:
                # SOURCE LINE 22
                __M_writer(u'   <tr> \n     <td colspan=3>\n     <table> \n        <tr>\n\t\t<th>Title</th>\n\t    <th>Query</th>\n\t    <th>Query Length</th>\n\t    </tr>\n\t         \n')
                # SOURCE LINE 31
                for alignment  in record.alignments: 
                    # SOURCE LINE 32
                    __M_writer(u'       <tr> \n         <td> ')
                    # SOURCE LINE 33
                    __M_writer(unicode(alignment.title ))
                    __M_writer(u' </td>\n         <td> ')
                    # SOURCE LINE 34
                    __M_writer(unicode(alignment.length ))
                    __M_writer(u' </td>\n         <td> ')
                    # SOURCE LINE 35
                    __M_writer(unicode(len(alignment.hsps) ))
                    __M_writer(u' </td>\n         <td> hsps.expect\n         <td> hsps.score\n         <td> hsps.query_start\n         <td> hsps.query_end\n       </tr>\n')
                # SOURCE LINE 42
                __M_writer(u'     </table>     \n\t  </td>\n      </tr>\n     \n')
        # SOURCE LINE 48
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


