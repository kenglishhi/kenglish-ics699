#!/usr/bin/python

from Bio import ExPASy
from Bio.WWW import *                                                     
from Bio.SwissProt import SProt

expasy = ExPASy.get_sprot_raw('CERU_HUMAN')
sp = SProt.Iterator(expasy, SProt.RecordParser())
record = sp.next()
print record.keywords

