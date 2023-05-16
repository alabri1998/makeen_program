# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:23:03 2023

@author: user
"""

dic = {'1': {"name" : "p1",
           "age" : 22
    },
       '2':{"name" : "p2",
           "age" : 27
           }}
for item in dic.items():
    print(item)
    second_dic = item[1]
    if second_dic['age'] > 22:
        print(second_dic['name'])