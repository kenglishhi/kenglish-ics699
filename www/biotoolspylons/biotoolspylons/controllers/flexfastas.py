import logging

from biotoolspylons.lib.base import *

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile

log = logging.getLogger(__name__)

class FlexfastasController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py file has
    # a resource setup:
    #     map.resource('flexfasta', 'flexfastas')


    def index(self, format='html'):
        """GET /flexfastas: All items in the collection."""
        # url_for('flexfastas')
        message = "They called index on flexfastas"
        log.debug(message)
        response.headers['Content-type'] = "text/xml" 
        c.fasta_files =  fastafile.get_fasta_files() 
        return render('/flexfastas/index_flexfasta.xml.mako')


    def create(self):
        """POST /flexfastas: Create a new item."""
        # url_for('flexfastas')
        message = "They called file upload " + request.POST["Filedata"].filename
        log.debug(message)
        uploadfile = request.POST["Filedata"]
        fasta_file = open(os.path.join(permanent_store,
                                           uploadfile.filename.lstrip(os.sep)),
                                           'w')

        shutil.copyfileobj(uploadfile.file, fasta_file)    
        uploadfile.file.close()
        fasta_file.close()
        fastafile.formatdb(fasta_file.name)


    def new(self, format='html'):
        """GET /flexfastas/new: Form to create a new item."""
        # url_for('new_flexfasta')
        pass

    def update(self, id):
        """PUT /flexfastas/id: Update an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(h.url_for('flexfasta', id=ID),
        #           method='put')
        # url_for('flexfasta', id=ID)
        pass

    def delete(self, id):
        """DELETE /flexfastas/id: Delete an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(h.url_for('flexfasta', id=ID),
        #           method='delete')
        # url_for('flexfasta', id=ID)
        pass

    def show(self, id, format='html'):
        """GET /flexfastas/id: Show a specific item."""
        # url_for('flexfasta', id=ID)
        pass

    def edit(self, id, format='html'):
        """GET /flexfastas/id;edit: Form to edit an existing item."""
        # url_for('edit_flexfasta', id=ID)
        pass
