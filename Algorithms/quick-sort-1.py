#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:14:08 2017

@author: venkatapochiraju
"""

n = int(input())
ar = list(map(int,input().split()))
p = ar[0]
left, right, equal = [], [], []
for i in range(n):
    if ar[i] == p:
        equal.append(ar[i])
    elif ar[i] > p:
        right.append(ar[i])
    else:
        left.append(ar[i])
print(*left, end = " ")
print(*equal, end = " ")
print(*right)
