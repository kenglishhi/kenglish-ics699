#!/usr/bin/python

enz=[]
def add_enz(*new):
    global enz
    enz = enz + list(new)

add_enz('EcoRI')
add_enz('HindIII')
add_enz('BamHI')
print enz
