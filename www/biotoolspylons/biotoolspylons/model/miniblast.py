import os,re

from biotoolspylons.model import fastafile
from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML

BLAST_EXE =  "/usr/bin/blastall"
BLAST_PROGRAM =  "blastn"

def blast_2_files(input_filename,input_db):
    blast_db = fastafile.PERMANENT_STORE + input_db
    blast_file = fastafile.PERMANENT_STORE + input_filename
    if not os.path.exists(blast_db + ".nin"):
        fastafile.formatdb(blast_db)

    blast_out, error_handle = NCBIStandalone.blastall(BLAST_EXE, BLAST_PROGRAM, blast_db, blast_file)
    return blast_out 

def save_results(save_filename,results_handle):
    save_filename = fastafile.PERMANENT_STORE + save_filename
    blast_results = results_handle.read()

    save_file = open(save_filename, 'w')
    save_file.write(blast_results)
    save_file.close()
    return

def make_output_filename(input_filename,input_db):
    return os.path.basename(input_filename) + "_vs_" + os.path.basename(input_db) + ".xml" 

def read_results(xml_filename):
    blast_out = open(fastafile.PERMANENT_STORE + xml_filename, "r") 
    records = NCBIXML.parse(blast_out)
    results  = []
    while True:
        try:
            b_record = records.next()
            results.append(b_record)
        except StopIteration:
            break
    blast_out.close() 
    return results


