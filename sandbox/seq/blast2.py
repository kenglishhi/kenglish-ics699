#!/usr/bin/python

my_blast_db = "/home/kenglish/Data/Genomes/Databases/EST_Clade_A"
my_blast_file = "m_cold.fasta"
my_blast_exe = "/usr/bin/blastall"

from Bio.Blast import NCBIStandalone

result_handle, error_handle = NCBIStandalone.blastall(my_blast_exe, "blastn", my_blast_db, my_blast_file)

blast_results = result_handle.read()

save_file = open("my_blast.xml", "w")
save_file.write(blast_results)
save_file.close()

