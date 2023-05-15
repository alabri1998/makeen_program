# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    sum_digit = sum_digits(234)
    print(sum_digit)
    
def sum_digits(number):
    number = str(number)
    sum=0
    for i in number:
        sum = sum + int(i)
    return sum
main()