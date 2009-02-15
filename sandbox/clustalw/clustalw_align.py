#!/usr/bin/python


from Bio.Alphabet import IUPAC
from Bio.Clustalw import *
from sys import *


fasta_file = '/home/kenglish/Data/Genomes/Databases/EST_Clade_C_3.fasta'
cline = MultipleAlignCL(fasta_file, command='/usr/bin/clustalw')      
cline.set_output('/home/kenglish/Data/Genomes/Databases/clustalw_align_test.aln')
print "Command line: ", cline

align = do_alignment(cline)                                             
for seq in align.get_all_seqs():                                       
    print seq.description
    print seq.seq
	    
