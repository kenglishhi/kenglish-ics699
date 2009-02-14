import logging

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile 
from biotoolspylons.model import miniblast 
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

        if  request.POST['fasta_filename1'] == request.POST['fasta_filename2'] :

            session['flash'] = 'Files should not be identical successfully updated.'
            session.save()
            redirect_to(action='index',fasta_filename1=request.POST['fasta_filename1'],fasta_filename2=request.POST['fasta_filename2'])

        fasta_db = request.POST['fasta_filename1'] 
        fasta_filename = request.POST['fasta_filename2'] 

        blast_out = miniblast.blast_2_files(fasta_filename,fasta_db)
        blast_result_xml = miniblast.make_output_filename(fasta_filename,fasta_db)
        miniblast.save_results(blast_result_xml, blast_out)
        c.blast_results = miniblast.read_results(blast_result_xml )

#        blast_out, error_handle = NCBIStandalone.blastall(blast_exe, blast_program, blast_db, blast_file)
#        records = NCBIXML.parse(blast_out)
#        c.results  = [] 
#
#        while True:
#            try:
#                b_record = records.next()
#                c.results.append(b_record) 
#            except StopIteration:
#                break

        return render('/miniblast/blast_miniblast.mako')

