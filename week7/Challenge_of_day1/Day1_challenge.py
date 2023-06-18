# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 13:24:15 2023

@author: alabri1998
"""
def gender_identifier(name):
    lst = []
    for el in name:
        lst.append(el.lower())
    
    non_repeated = []
    for i in lst:
        if i not in non_repeated and lst.count(i) == 1:
            non_repeated.append(i)
    print(non_repeated)
    if len(non_repeated)%2 == 0:
        print('this is a girl')
    else:
        print('this is a boy')

gender_identifier("jamal")