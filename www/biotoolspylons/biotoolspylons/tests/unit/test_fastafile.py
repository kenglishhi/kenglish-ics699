import sys
import nose

sys.path.append('/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons')

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile
from biotoolspylons.model.fastafile import FastaFile
from biotoolspylons.model import miniblast
from biotoolspylons.model.pathinfo import *
from pylons import config


def test_fastfile():
    files = fastafile.get_fasta_files()
    assert files[0].filename
    assert files[0].size
    assert files[0].to_xml() 
#    assert collection_to_xml()
        
def test_sequence_count():
    file = fastafile.PERMANENT_STORE + "EST_Clade_A_5.fasta" 
    fasta = FastaFile( file )
    nose.tools.assert_equal(fasta.sequence_count(),  5)

def test_sequences():
    fasta = FastaFile("/home/kenglish/Data/uploads/EST_Clade_A_5.fasta")
    sequences = fasta.get_sequences() 
    nose.tools.assert_equal( len(sequences ), 5 )
    nose.tools.assert_equal( sequences[0].id,  "1420338:1")
    nose.tools.assert_equal( len(sequences[0]) , 302 )

def test_sequences2():
    fasta = FastaFile("/home/kenglish/Data/uploads/EST_Clade_A.fasta")
    sequences = fasta.get_sequences() 
    nose.tools.assert_equal( len(sequences ), 2163 )
    nose.tools.assert_equal( sequences[0].id,  "1420338:1")
    nose.tools.assert_equal( len(sequences[0]) , 302 )
