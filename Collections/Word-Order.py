#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:08:26 2017

@author: venkatapochiraju
"""

d={}
n = int(input())
for i in range(n):
	s=input().rstrip()
	if s not in d: d[s]=[i,0]
	d[s][1]+=1
print(len(d))
print(' '.join(str(a[1]) for a in sorted(d.values())))
