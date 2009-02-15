#!/usr/bin/python

import Bio.Fasta
import sys

handle  = open(sys.argv[1]) 
it = Bio.Fasta.Iterator(handle, Bio.Fasta.SequenceParser())
seq = it.next()
while seq:
  print seq.description
  print seq.seq
  seq = it.next()
handle.close()

