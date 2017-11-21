#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:09:02 2017

@author: venkatapochiraju
"""

from collections import deque

d = deque()
N = int(input())
for i in range(N):
	names, *values = input().split()
	getattr(d, names)(*values)
print (*[item for item in d], sep = " ")
