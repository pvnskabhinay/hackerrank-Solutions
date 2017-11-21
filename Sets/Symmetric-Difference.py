#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:42:11 2017

@author: venkatapochiraju
"""

M = input()
a = input()
a_list = a.split()
a_list = list(map(int, a_list))
a_set = set(a_list)
N = input()
b = input()
b_list = b.split()
b_list = list(map(int, b_list))
b_set = set(b_list)
a_set1 = a_set.difference(b_set)
b_set1 = b_set.difference(a_set)
final_set = a_set1.union(b_set1)
final_list = list(final_set)
final_list.sort()
for e in final_list:
    print(e)
