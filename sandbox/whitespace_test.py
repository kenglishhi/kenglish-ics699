#!/usr/bin/python

from string import *

dna = """ 
aaattcctga gccctgggtg caaagtctca gttctctgaa atcctgacct aattcacaag
ggttactgaa gatttttctt gtttccagga cctctacagt ggattaattg gccccctgat
tgtttgtcga agaccttact tgaaagtatt caatcccaga aggaagctgg aatttgccct
tctgtttcta gtttttgatg agaatgaatc ttggtactta gatgacaaca tcaaaacata
ctctgatcac cccgagaaag taaacaaaga tgatgaggaa ttcatagaaa gcaataaaat
gcatggtatg tcacattatt ctaaaacaa """
print "BEFORE:" 
print dna  
for s in whitespace:
     dna = replace(dna, s, "")

print "AFTER:" 
print dna
