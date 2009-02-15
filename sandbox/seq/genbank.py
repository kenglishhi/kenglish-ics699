#!/usr/bin/python


from Bio import GenBank
ncbi_dict = GenBank.NCBIDictionary(database="nucleotide", format="genbank")
gb_entry = ncbi_dict['AB000001']

print gb_entry
