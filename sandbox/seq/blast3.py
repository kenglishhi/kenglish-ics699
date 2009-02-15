#!/usr/bin/python

my_blast_db = "/home/kenglish/Data/Genomes/Databases/EST_Clade_A"
my_blast_file = "Record1.fasta"
my_blast_exe = "/usr/bin/blastall"

from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML


result_handle, error_handle = NCBIStandalone.blastall(my_blast_exe, "blastn", my_blast_db, my_blast_file)

blast_results = result_handle.read()
print blast_results

#blast_records = NCBIXML.parse(result_handle)
#for blast_record in blast_records:
#    print blast_record
#print len(blast_results.alignments)
#save_file = open("my_blast.xml", "w")
#save_file.write(blast_results)
#save_file.close()

