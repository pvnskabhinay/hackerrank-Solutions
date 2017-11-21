#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:09:18 2017

@author: venkatapochiraju
"""

import sys, collections
from collections import deque 
T = int(input())
for i in range(T):
    n = int(input())
    lengths = deque(map(int, input().split()))
    max_length = max(lengths)
    while len(lengths) > 0:
        l = lengths[0]
        r = lengths[-1]
        if r <= max_length and r >= l:
            max_length = r
            lengths.pop()
        elif l <= max_length and l >= r:
            max_length = l
            lengths.popleft()
        else:
            break
    if len(lengths) == 0:
        print("Yes")
    else: 
        print("No")
