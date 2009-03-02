import os,re
import pyxslt.serialize
from biotoolspylons.model.pathinfo import *
from Bio import SeqIO

PERMANENT_STORE = '/home/kenglish/Data/uploads/'

def formatdb(fasta_file):

    db_name = fasta_file
    cmd = "formatdb -i %s -p F -o F" % fasta_file
    output = os.system(cmd)

def get_fasta_files():
    fasta_files = []
    for filename in os.listdir(PERMANENT_STORE):
        if re.compile('.*fasta$').match(filename):
            fasta_files.append(FastaFile(PERMANENT_STORE + filename))
    fasta_files.sort()
    return fasta_files 
#def collection_to_xml(array):
#    return pyxslt.serialize.toString(prettyPrintXml=True, fastafiles=array)
    

class FastaFile(PathInfo):

    def to_xml(self): 
        return pyxslt.serialize.toString(prettyPrintXml=True, fastafile=self)

    def sequence_count(self):
        regex = re.compile(r'>')
        file = open(self.path) 
        count =0
        for line in file:
            four_letter_words = regex.findall(line)
            for word in four_letter_words:
                count = count + 1
        file.close
        return count

    def get_sequences(self):
        try: self.sequences
        except AttributeError:
            self.sequences = [] 
            handle = open(self.path)
            for seq_record in SeqIO.parse(handle, "fasta") :
                self.sequences.append(seq_record) 
            handle.close()
        return self.sequences
