# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:20:05 2019

@author: Ahmad Luthfi Mahar
"""
def nomor_3(baris):
    titik0 = (2*(baris-1))+1
    for i in range(baris):
        for k in range(titik0):
            if i == 0:
                print("*", end="")
            elif k == i or k == titik0-i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

nomor_3(4)