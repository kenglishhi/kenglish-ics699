import sys
sys.path.append('/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons')

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile
from biotoolspylons.model import miniblast

import Bio.Fasta
from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML

fasta_db = 'EST_Clade_A_1.fasta' 
fasta_filename = 'EST_Clade_A_1.fasta' 

blast_out = miniblast.blast_2_files(fasta_filename,fasta_db) 
blast_result_xml = miniblast.make_output_filename(fasta_filename,fasta_db) 
miniblast.save_results(blast_result_xml, blast_out)
blast_results = miniblast.read_results(blast_result_xml )

record= blast_results[0]

for attr in dir(record):
    print "%s = %s " % (attr,  getattr(record, attr) )

