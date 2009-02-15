#!/usr/bin/python


base = "e"
if base in "atgc":
    print "exact"
elif base in "bdhkmnrsuvwxy":
    print "ambiguous"
else:
    print "unknown"


