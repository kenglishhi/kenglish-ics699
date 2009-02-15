import Bio.Clustalw
from Bio.Alphabet import IUPAC
from sys import *

clustal_output_file = "/home/kenglish/Data/Genomes/Databases/EST_Clade_A_2.aln"

align = Bio.Clustalw.parse_file( clustal_output_file, alphabet=IUPAC.unambiguous_dna )

for seq in align.get_all_seqs():
    print seq.description
    print seq
