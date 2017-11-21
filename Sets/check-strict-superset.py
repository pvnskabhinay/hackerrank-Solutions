#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:47:00 2017

@author: venkatapochiraju
"""

import sys
A = set(map(int, input().split()))
n = int(input())
for i in range(n):
    set1 = set(map(int, input().split()))
    if (A.issuperset(set1) != True) or (len(A) == len(set1)): 
        print(False)
        sys.exit() 
else: print(True)
