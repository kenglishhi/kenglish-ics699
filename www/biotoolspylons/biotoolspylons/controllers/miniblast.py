import logging

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile 
import Bio.Fasta
from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML

log = logging.getLogger(__name__)

class MiniblastController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        c.fasta_files =  fastafile.get_fasta_files()
        return render('/miniblast/index_miniblast.mako')
    def blast(self):
        blast_exe =  "/usr/bin/blastall"
        blast_program =  "blastn"
        if  request.POST['file1'] == request.POST['file2'] :
            session['flash'] = 'Files should not be identical successfully updated.'
            session.save()
            redirect_to(action='index',file1=request.POST['file1'],
            file2=request.POST['file2'], )

        blast_db = fastafile.PERMANENT_STORE + request.POST['file1'] 
        blast_file = fastafile.PERMANENT_STORE + request.POST['file2'] 

        blast_out, error_handle = NCBIStandalone.blastall(blast_exe, blast_program, blast_db, blast_file)
        records = NCBIXML.parse(blast_out)
        c.results  = [] 
        while True:
            try:
                b_record = records.next()
                c.results.append(b_record) 
            except StopIteration:
                break
        return render('/miniblast/blast_miniblast.mako')
