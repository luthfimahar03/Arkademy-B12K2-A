# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:13:10 2019

@author: Ahmad Luthfi Mahar
"""

def nomor_4(inp):
    def check_arranged(_to_arrange):
        to_arrange = _to_arrange.split("-")
        if len(to_arrange[-1]) == 1:
            to_complete = to_arrange[-2][-1]
            to_complete += to_arrange[-1]
            to_arrange[-1] = to_complete
            to_arrange[-2] = to_arrange[-2][:-1]
            _to_arrange = "-".join(to_arrange)
        return _to_arrange
    inp = str(inp)
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
    arranged = check_arranged(arranged)
    return arranged
print(nomor_4("993141 -1 1323 14-232"))

