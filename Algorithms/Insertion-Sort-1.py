#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:14:55 2017

@author: venkatapochiraju
"""

size = int(input())
arr = list(map(int, input().split()))
i = size - 2
x = arr[size - 1]
while i >= 0 and arr[i] > x:
    arr[i + 1] = arr[i]
    i -= 1
    print(*arr)
arr[i + 1] = x
print(*arr)
