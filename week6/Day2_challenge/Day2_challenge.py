# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:20:12 2023

@author: alabri1998
"""
def progress(lst):
    prog_count = 0
    for i in lst:
        try:
            if lst[i] < lst[i+1]:
                prog_count+=1
            else:
                continue
        except IndexError:
            break
    return prog_count
ls = [2,4,7,10,8,11]
result = progress(ls) + 2
print(result)
ls = [5,7,6,9,8]
result = progress(ls) + 2
print(result)