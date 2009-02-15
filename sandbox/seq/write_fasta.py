#!/usr/bin/python


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import Bio.writers.SeqRecord.fasta
import Bio.Alphabet
from sys import *



dna = Seq('gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg',Bio.Alphabet.DNAAlphabet())
seq = SeqRecord(dna, id = 'my_seq', description= 'a random sequence') 
fasta_writer = Bio.writers.SeqRecord.fasta.WriteFasta(stdout)  
fasta_writer.write(seq)
