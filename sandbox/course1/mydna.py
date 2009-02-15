#!/local/bin/python

def ambiguous_dna_alphabet():
    " returns a string containing all ambiguous dna bases "
    return "bdhkmnrsuvwxy"

def all_2_digests(enzymes):
    """ generate all possible digests with 2 enzymes """

    digests = []
    for i in range(len(enzymes)):
        print "i =",i
        for k in range(i+1, len(enzymes)):
            print "k = ",k 
            digests.append( [enzymes[i], enzymes[k]] )
    return digests


dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg'
print dna
print dna.upper()

digest = all_2_digests(['EcoRI', 'HindIII', 'BamHI'])
print digest

