#!/usr/bin/python

f = open("seqs.fasta")

entry = get_fasta(f)
while entry:
    entry = get_fasta(f)

f.close()

