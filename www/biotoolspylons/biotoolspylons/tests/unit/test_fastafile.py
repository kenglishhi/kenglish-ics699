import sys
import nose

sys.path.append('/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons')


from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile
from biotoolspylons.model.fastafile import FastaFile
from biotoolspylons.model import miniblast
from biotoolspylons.model.pathinfo import *


def test_fastfile():
    files = fastafile.get_fasta_files()
    assert files[0].filename
    assert files[0].size
    assert files[0].to_xml() 
#    assert collection_to_xml()
        
def test_sequence_count():
    fasta = FastaFile("/home/kenglish/downloads/uploads/EST_Clade_A_5.fasta")
    nose.tools.assert_equal(fasta.sequence_count(),  5)
