#!/usr/bin/python


from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

result_handle = open("my_blast.xml")
blast_records = NCBIXML.parse(result_handle)

for blast_record in blast_records:
    print blast_record
    


