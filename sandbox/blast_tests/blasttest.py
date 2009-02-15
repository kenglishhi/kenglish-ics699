#!/usr/bin/python
import sys
import os
import Bio.Fasta
from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML


def formatdb(fasta_file):
    db_name = fasta_file
    cmd = "formatdb -i %s -p F -o F" % fasta_file
    output = os.system(cmd)
    print "output: %s " % output

blast_exe =  "/usr/bin/blastall"
blast_program =  "blastn"
blast_file = sys.argv[1] 
blast_db = sys.argv[2] 

print "blast_file:", blast_file, "blast_db:", blast_db
formatdb(blast_db) 

handle = open(blast_file)
query_sequences = {} 
it = Bio.Fasta.Iterator(handle, Bio.Fasta.SequenceParser())
seq = it.next()
while seq:
  query_sequences[seq.description] = {} 
  query_sequences[seq.description]["number_of_hits"] = 0 
  print seq.description
  print query_sequences[seq.description]["number_of_hits"] 
  seq = it.next()

handle.close()




blast_out, error_handle = NCBIStandalone.blastall(blast_exe, blast_program, blast_db, blast_file)

#print error_handle 

records = NCBIXML.parse(blast_out)

#b_record = records.next() 
#
#
#E_VALUE_THRESH = 0.000000004
#
#print  dir(b_record)
#print  b_record.num_sequences
#print "Query = %s"  % b_record.query

#b_record = records.next() 

while True:
    try:
        b_record = records.next()
        print "Query = %s"  % b_record.query
    except StopIteration:
        break

#for alignment in b_record.alignments:
#    for hsp in alignment.hsps:
#        if hsp.expect < E_VALUE_THRESH:
#         print '****Alignment****'
#         print 'sequence:', alignment.title
#         print 'length:', alignment.length
#         print 'e value:', hsp.expect
#         print hsp.query[0:75] + '...'
#         print hsp.match[0:75] + '...'
#         print hsp.sbjct[0:75] + '...'
#
#quit()
#blast_results = blast_out.read()
#
#
#save_file = open("my_blast.xml", "w")
#save_file.write(blast_results)
#save_file.close()
#
#
#out, error = NCBIStandalone.blastall(\
#   "blastall", "blastn",
#   "nr", "to_blast.fasta")
#parser = NCBIStandalone.BlastParser()
#rec = parser.parse(blast_out)
#print rec.descriptions[0].title
#quit()
#

#blast_out = open("my_blast.xml", "r")
##
#b_parser = NCBIStandalone.BlastParser()
#b_record = b_parser.parse(blast_out)
#blast_out.close()
