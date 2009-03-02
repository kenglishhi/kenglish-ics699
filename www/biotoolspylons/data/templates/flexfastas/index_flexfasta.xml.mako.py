from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1235630012.483885
_template_filename='/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons/biotoolspylons/templates/flexfastas/index_flexfasta.xml.mako'
_template_uri='/flexfastas/index_flexfasta.xml.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<?xml version="1.0" encoding="UTF-8"?>\n<fastafiles>\n')
        # SOURCE LINE 3
        for fasta in c.fasta_files:
            # SOURCE LINE 4
            __M_writer(u'  <fastafile>\n    <filename>')
            # SOURCE LINE 5
            __M_writer(unicode(fasta.filename))
            __M_writer(u'</filename>\n    <size>')
            # SOURCE LINE 6
            __M_writer(unicode(fasta.size))
            __M_writer(u'</size>\n    <mod_time>')
            # SOURCE LINE 7
            __M_writer(unicode(fasta.modTime()))
            __M_writer(u'</mod_time>\n    <sequence_count>')
            # SOURCE LINE 8
            __M_writer(unicode(fasta.sequence_count()))
            __M_writer(u'</sequence_count>\n\n  </fastafile>\n')
        # SOURCE LINE 12
        __M_writer(u'</fastafiles>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


