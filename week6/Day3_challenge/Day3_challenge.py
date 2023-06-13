# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:14:05 2023

@author: alabri1998
"""
def calculate_length(arr):
    total_length = 0
    for item in arr:
        if isinstance(item, list):
            total_length += calculate_length(item)
        else:
            total_length += 1
    return total_length

arr = [1, [2, 3]]
length = calculate_length(arr)
print(length)  
arr = [1, [2, 3,[5,5,6]]]
length = calculate_length(arr)
print(length)
