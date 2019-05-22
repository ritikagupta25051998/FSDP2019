# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:41:05 2019

@author: HP WORLD
"""

fp =  open("ritika.txt","r")

str1 = fp.read()

fout = open("mahi.txt", "w")
fout.write(str1)
fout.flush()

#---------------------------
with open("ritika.txt", "r") as fin:
    with open("mahi.txt", 'w') as fout:
        for line in fin:
            fout.write(line)
     
        

    
