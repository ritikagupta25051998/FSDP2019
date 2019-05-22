# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:41:05 2019

@author: HP WORLD
"""
file=open("ritika.txt","rt")
print(file.read())
with open("ritika.txt","rt") as rf:
    open("mahi.txt","wt") as wf:
    for line in rf:
        wf.write(line)
    
