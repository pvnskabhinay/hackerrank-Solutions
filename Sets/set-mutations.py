#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:45:30 2017

@author: venkatapochiraju
"""

length_a = int(input())
a = set(map(int,input().split()))
N = int(input())
for i in range(N):
    n1 , n2 = input().split()
    temp = set(map(int,input().split()))
    if n1 == "intersection_update":
        a.intersection_update(temp)
    elif n1 == "update":
        a.update(temp)
    elif n1 == "symmetric_difference_update":
        a.symmetric_difference_update(temp)
    elif n1 == "difference_update":
        a.difference_update(temp)
print(sum(a))
