import logging

from biotoolspylons.lib.base import *

import os, re, shutil 
import biotoolspylons.lib.helpers as h
import Bio.Fasta


permanent_store = '/home/kenglish/downloads/uploads/'
log = logging.getLogger(__name__)

class FastasController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py file has
    # a resource setup:
    #     map.resource('fasta', 'fastas')


    def index(self, format='html'):
        """GET /fastas: All items in the collection."""
        c.fasta_files = []
        for filename in os.listdir(permanent_store):
            if re.compile('.*fasta$').match(filename):
                c.fasta_files.append( filename ) 
        c.links = [ 'James', 'Ben', 'Philip' ]
        return render('/fastas/index_fasta.mako')

    def create(self):
        """POST /fastas: Create a new item."""
        # url_for('fastas')

        uploadfile = request.POST['uploadfile']
        fasta_file = open(os.path.join(permanent_store,
                                           uploadfile.filename.lstrip(os.sep)),
                                           'w')

        shutil.copyfileobj(uploadfile.file, fasta_file)
        uploadfile.file.close()
        fasta_file.close()
        handle = open( fasta_file.name )
#        if false:
        it = Bio.Fasta.Iterator(handle, Bio.Fasta.SequenceParser())
        seq = it.next()
        c.sequences = [] 
        output_string = "" 
        while seq:
            c.sequences.append(seq) 
            output_string += seq.description 
            output_string += "<br /> " 
            log.debug("seq : %s" ,  seq.description) 
            seq = it.next()

        handle.close()
        self.formatdb(fasta_file.name) 

        log.debug('Hello Kenglish' )
        print "Hello Kenglish" 

        return render('/fastas/created_fasta.mako')
        return 'Successfully uploaded: %s, description: %s, <br /> results: <br /> %s ' % \
            (uploadfile.filename, request.POST['description'], output_string)

    def formatdb(self,fasta_file):
        db_name = fasta_file
        cmd = "formatdb -i %s -p F -o F" % fasta_file
        output = os.system(cmd)
        print "output: %s " % output



    def new(self, format='html'):
        """GET /fastas/new: Form to create a new item."""
        # url_for('new_fasta')
        return render('/fastas/new_fasta.mako')

    def update(self, id):
        """PUT /fastas/id: Update an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(h.url_for('fasta', id=ID),
        #           method='put')
        # url_for('fasta', id=ID)
        pass

    def delete(self, id):
        """DELETE /fastas/id: Delete an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(h.url_for('fasta', id=ID),
        #           method='delete')
        # url_for('fasta', id=ID)
        pass

    def show(self, id, format='html'):
        """GET /fastas/id: Show a specific item."""
        # url_for('fasta', id=ID)
        pass

    def edit(self, id, format='html'):
        """GET /fastas/id;edit: Form to edit an existing item."""
        # url_for('edit_fasta', id=ID)
        pass



