from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1234421452.8444531
_template_filename='/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons/biotoolspylons/templates/fastas/new_fasta.mako'
_template_uri='/fastas/new_fasta.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n\n\n<h1>Upload Fasta</h1>\n\n<p>Select a file from your filesystem to upload</p>\n\n')
        # SOURCE LINE 13
        __M_writer(unicode(h.rails.form(h.url_for(action='create' ), method='POST',multipart=True)))
        __M_writer(u'\nUpload file: ')
        # SOURCE LINE 14
        __M_writer(unicode(h.rails.file_field('uploadfile')))
        __M_writer(u' <br />\n')
        # SOURCE LINE 15
        __M_writer(unicode(h.rails.submit('Submit')))
        __M_writer(u'<br /> \n</form>\n')
        # SOURCE LINE 17
        __M_writer(unicode(h.rails.end_form()))
        __M_writer(u'\n')
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


