import Bio.Clustalw
from Bio.Alphabet import IUPAC
from sys import *

align = Bio.Clustalw.parse_file( argv[1], alphabet=IUPAC.unambiguous_dna )

for seq in align.get_all_seqs():
    print seq.description
    print seq
