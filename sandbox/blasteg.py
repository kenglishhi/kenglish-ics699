#!/usr/bin/python

params = { 'e': 1.0, 'm': 8, 'F': 'S 10 1.0 1.5' }


def blast2(query, program='blastp', database='swissprot', params=params):
    command = "blastall -p %s -d %s -i %s" % (program, database, query)
    if params:
        for para, value in params.items():
             command += " -%s '%s'" % (para, value)   
    return command 

print blast2("seq.fasta")
print blast2("seq.fasta", "blastp", "nprot")
