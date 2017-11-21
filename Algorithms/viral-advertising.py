#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:13:38 2017

@author: venkatapochiraju
"""

n = int(input())
total = 5
liketotal = 0
for i in range(n):
    like = int(total/2)
    liketotal += like
    total = like*3
print(liketotal)
