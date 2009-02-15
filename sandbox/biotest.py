#!/usr/bin/python
import Bio.Fasta

handle = open("seqs.fasta")

it = Bio.Fasta.Iterator(handle, Bio.Fasta.SequenceParser())

seq = it.next() 
while seq:
    print seq.seq
    print seq.description
    seq = it.next() 
handle.close()
