# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:24:14 2023

@author: alabri1998
"""
def print_numbers_greater_or_equal(nums):
    for i in range(len(nums)):
        greater_or_equal = True
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                greater_or_equal = False
                break
        if greater_or_equal:
            print(nums[i])

# مثال الإدخال الأول
input1 = [1, 4, 5, 7, 3, 0]
print_numbers_greater_or_equal(input1)
print()
# مثال الإدخال الثاني
input2 = [1, 2, 3, 4]
print_numbers_greater_or_equal(input2) 
