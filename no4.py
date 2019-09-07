# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:13:10 2019

@author: Ahmad Luthfi Mahar
"""

def nomor_4(inp):
    arranged = ""
    i = 0
    for seq in inp.split(" "):
        for seq2 in seq.split("-"):
            for c in seq2:
                arranged += c
                i += 1
                if i == 3:
                    arranged += "-"
                    i = 0
    return arranged
print(nomor_4("993141 -1 1323 14-232"))

