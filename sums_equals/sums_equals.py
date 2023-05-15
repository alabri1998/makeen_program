# -*- coding: utf-8 -*-
"""
Created on Mon May 15 20:02:53 2023

@author: alabri1998
"""
def can_divide_arr(arr):
    # Calculate the sum of all elements in the array
    total_sum = sum(arr)

    # If the total sum is odd, it can't be divided into two subarrays with equal sums
    if total_sum % 2 == 1:
        return False

    # Calculate the target sum that each subarray should have
    target_sum = total_sum // 2

    # Create a set to store all possible sums that can be achieved by subsets of the array
    possible_sums = {0}

    # Iterate over all elements in the array
    for num in arr:
        # Create a new set to store all possible sums that can be achieved by adding the current element
        new_sums = set()
        for possible_sum in possible_sums:
            # Calculate the new sum that can be achieved by adding the current element
            new_sum = possible_sum + num
            # If the new sum equals the target sum, we have found a solution
            if new_sum == target_sum:
                return True
            # Add the new sum to the set of possible sums
            new_sums.add(new_sum)
        # Add the new set of possible sums to the set of all possible sums
        possible_sums.update(new_sums)
    # If no solution was found, return False
    return False

arr = [2, 6, 1, 9]

print(can_divide_arr(arr))  # Output: True
arr = [ 6, 7, 2]
print(can_divide_arr(arr))  # Output: False