#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:09:36 2017

@author: venkatapochiraju
"""

cube = lambda x: x**3 

def fibonacci(n):
    if n == 0:
        fibNums = []
    elif n == 1:
        fibNums = [0]
    else:
        fibNums = [0,1]
    for i in range(n-len(fibNums)):
        fibNums.append(fibNums[-1]+fibNums[-2])
    return fibNums
