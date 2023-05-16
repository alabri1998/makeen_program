# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:26:15 2023

@author: user
"""


def main():
    sides = int(input("Enter number of sides: "))
    counters = countInputs(sides)
    printCounters(counters)
    


def countInputs(side):
    counters = [0]*(side+1)
    nard = input("input nard values , Q to quit: ")
    while nard.upper() != "Q":
        for i in range(1,side+1):
            if int(nard) == i:
                counters[i] = counters[i]+1
        nard = input("input nard values , Q to quit: ")
            
    return counters
def printCounters(count):
    for i in range(1,len(count)):
        print(str(i) + " : "+str(count[i]))
main()