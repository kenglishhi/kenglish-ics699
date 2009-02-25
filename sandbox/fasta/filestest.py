import sys
sys.path.append('/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons')
#sys.path.append('/home/kenglish/workspace/kenglish-ics699/sandbox/blast_tests')

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile
from biotoolspylons.model import miniblast
from biotoolspylons.model.pathinfo import *

#import Bio.Fasta
#from Bio.Blast import NCBIStandalone
#from Bio.Blast import NCBIXML
#
files = fastafile.get_fasta_files()
for file in files:
    print file.filename
    print file.size
#    fileinfo = PathInfo(file)
#    print fileinfo

#p = PathInfo("/home/kenglish/downloads/uploads/EST_Clade_A_1.fasta")
#print p

