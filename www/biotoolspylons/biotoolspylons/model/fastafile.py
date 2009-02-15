import os,re

PERMANENT_STORE = '/home/kenglish/downloads/uploads/'

def formatdb(fasta_file):

    db_name = fasta_file
    cmd = "formatdb -i %s -p F -o F" % fasta_file
    output = os.system(cmd)

def get_fasta_files():

    fasta_files = []
    for filename in os.listdir(PERMANENT_STORE):
        if re.compile('.*fasta$').match(filename):
            fasta_files.append( filename ) 
    return fasta_files 

