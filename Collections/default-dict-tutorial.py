#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:07:07 2017

@author: venkatapochiraju
"""

from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
for i in range(1,n+1,1):
    A[input()].append(i)
for i in range(1,m+1,1):
    b = input()
    length = len(A[b])
    if length > 0:
        print(" ".join(str(c) for c in A[b]))
    else:
        print(-1)
