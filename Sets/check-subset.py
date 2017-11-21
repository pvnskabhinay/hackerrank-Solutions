#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:46:30 2017

@author: venkatapochiraju
"""

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    if B.intersection(A)==A:
        print (True) 
    else:
        print(False)
