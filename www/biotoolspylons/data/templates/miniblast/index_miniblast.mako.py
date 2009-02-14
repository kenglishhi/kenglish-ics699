from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234585626.1608689
_template_filename='/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons/biotoolspylons/templates/miniblast/index_miniblast.mako'
_template_uri='/miniblast/index_miniblast.mako'
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
        __M_writer(u'\n\n<h1>Blast 2 files</h1>\n\n<p>Select 2 file to blast</p>\n\n')
        # SOURCE LINE 11
        __M_writer(unicode(h.rails.form(h.rails.url(action='blast' ), method='POST',multipart=True)))
        __M_writer(u'\n')
        # SOURCE LINE 12
        flash_message = h.flash.pop_message()  
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['flash_message'] if __M_key in __M_locals_builtin()]))
        __M_writer(u'\n')
        # SOURCE LINE 13
        if flash_message:
            # SOURCE LINE 14
            __M_writer(u'<div id="flash-message">')
            __M_writer(filters.html_escape(unicode(flash_message )))
            __M_writer(u'</div>\n')
        # SOURCE LINE 16
        __M_writer(u'\nFile1: ')
        # SOURCE LINE 17
        __M_writer(unicode( h.rails.select('fasta_filename1' , h.options_for_select( c.fasta_files ) )  ))
        __M_writer(u' <br />\nFile2: ')
        # SOURCE LINE 18
        __M_writer(unicode( h.rails.select('fasta_filename2' , h.options_for_select( c.fasta_files ) )  ))
        __M_writer(u' <br />\n\n')
        # SOURCE LINE 20
        __M_writer(unicode(h.rails.submit('Submit')))
        __M_writer(u'<br />\n</form>\n')
        # SOURCE LINE 22
        __M_writer(unicode(h.rails.end_form()))
        __M_writer(u'\n\n')
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


