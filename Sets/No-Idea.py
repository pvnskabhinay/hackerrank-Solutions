#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:42:40 2017

@author: venkatapochiraju
"""

n , m = map(int, input().split())
n_arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
h = 0
for e in n_arr:
    if e in a:
        h = h + 1
    elif e in b:
        h = h - 1

print(h)
