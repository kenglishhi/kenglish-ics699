#!/usr/bin/python

from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML
my_blast_db =   "/home/kenglish/Data/Genomes/Databases/EST_Clade_A"
my_blast_file = "/home/kenglish/Data/Genomes/Databases/EST_Clade_A_1.fasta"
my_blast_exe =  "/usr/bin/blastall"

blast_out, error_handle = NCBIStandalone.blastall(my_blast_exe, "blastn", my_blast_db, my_blast_file)
#print error_handle 


records = NCBIXML.parse(blast_out)
b_record = records.next() 

E_VALUE_THRESH = 0.000000004
for alignment in b_record.alignments:
    for hsp in alignment.hsps:
#        if hsp.expect < E_VALUE_THRESH:
         print '****Alignment****'
         print 'sequence:', alignment.title
         print 'length:', alignment.length
         print 'e value:', hsp.expect
         print hsp.query[0:75] + '...'
         print hsp.match[0:75] + '...'
         print hsp.sbjct[0:75] + '...'


quit()

#blast_results = blast_out.read()

#save_file = open("my_blast.xml", "w")
#save_file.write(blast_results)
#save_file.close()
#


#out, error = NCBIStandalone.blastall(\
#   "blastall", "blastn",
#   "nr", "to_blast.fasta")
parser = NCBIStandalone.BlastParser()
rec = parser.parse(blast_out)
print rec.descriptions[0].title
quit()


blast_out = open("my_blast.xml", "r")
#
b_parser = NCBIStandalone.BlastParser()
b_record = b_parser.parse(blast_out)
blast_out.close()
