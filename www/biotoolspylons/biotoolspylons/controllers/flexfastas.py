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
        response.headers['Content-type'] = "text/xml" 
        c.fasta_files =  fastafile.get_fasta_files() 
        return render('/flexfastas/index_flexfasta.xml.mako')
        return """\
<?xml version="1.0" encoding="UTF-8"?>
<fastafiles>
  <fastafile>
    <filename>EST_Clade_A_1.fasta</filename>
  </fastafile>
  <fastafile>
    <filename>EST_Clade_A_5.fasta</filename>
  </fastafile>
  <fastafile>
    <filename>EST_Clade_C_3.fasta</filename>
  </fastafile>
  <fastafile>
    <filename>EST_Clade_A.fasta</filename>        
  </fastafile>
</fastafiles>
"""


    def create(self):
        """POST /flexfastas: Create a new item."""
        # url_for('flexfastas')
        pass

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
