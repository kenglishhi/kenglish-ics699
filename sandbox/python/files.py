import glob, os, re

def fasta_files(dir):
    for filename in os.listdir(dir):
        if re.compile('.*fasta$').match(filename):
            print "yes %s" % filename 
