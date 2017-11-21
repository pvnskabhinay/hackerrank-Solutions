#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:15:44 2017

@author: venkatapochiraju
"""

s = int(input())
a = list(map(int, input().split()))
for i in range(1,s,1):
    x = [j for j in range(i) if a[j] > a[i]]
    index = next(iter(x), i)
    a[index+1:i+1], a[index] = a[index:i], a[i]
    print(*a)
