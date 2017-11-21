#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:05:58 2017

@author: venkatapochiraju
"""

import collections
from collections import Counter
import sys
X = int(input())
sizeColl = collections.Counter(map(int, input().split()))
N = int(input())
amount = 0
for i in range(N):
    size, xi = map(int,input().split())
    if (size in sizeColl and sizeColl[size]):
        sizeColl[size] = sizeColl[size] - 1
        amount = amount + xi

print(amount)
