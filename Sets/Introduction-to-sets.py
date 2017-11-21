#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:41:28 2017

@author: venkatapochiraju
"""

def average(array):
    N = len(array)
    if N > 0 & N <= 100:
        set1 = set(array)
        total = 0
        for e in set1:
            total = total + e
        l = len(set1)
        avg = total/l
    return avg
