#!/usr/bin/python


from Bio import ExPASy

ids = ['O23729', 'O23730', 'O23731']

all_results = ''
for id in ids:
    results = ExPASy.get_sprot_raw(id)
    all_results = all_results + results.read()

