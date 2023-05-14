# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:55:20 2023

@author: alabri1998
"""
arr = [1, 2, 7, 5, 8, 2, 1]
n = len(arr)

# Loop through the array and find the first non-repeating number
for i in range(n):
    is_unique = True
    for j in range(n):
        if i != j and arr[i] == arr[j]:
            is_unique = False
            break
    if is_unique:
        print(arr[i])
        break
else:
    print(None)
