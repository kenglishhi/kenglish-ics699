#!/usr/bin/python

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

my_sequence = """>My Sequence (in FASTA format)
MEMETIEEQSKCEMSITTLP

"""

print my_sequence 
qblast_output = NCBIWWW.qblast("blastp", "nr", my_sequence)

#result =  qblast_output.read()

parser = Bio.Blast.NCBIXML.parse NCBIXML.BlastParser()
result = parser.parse(qblast_output.read())

print len(result.alignments)
