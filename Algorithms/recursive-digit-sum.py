#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:15:18 2017

@author: venkatapochiraju
"""

def digit_sum(n):
    n = str(n)
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    else:
        return digit_sum(x)
import sys
inp = list(map(int,input().split()))
X = str(inp[0])
x = X
N = inp[1]
if (int(N)<1) and (int(N)>10**100000):
    sys.exit()
if (int(X) < 1) and (int(X) > 10**5):
    sys.exit()
for i in range(N-1):
    x += X
x = str(digit_sum(int(x)))
print(x)
