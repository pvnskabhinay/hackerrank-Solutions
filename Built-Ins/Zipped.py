#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:08:18 2017

@author: venkatapochiraju
"""

N,X = map(int, raw_input().split())
subject_list = []
for i in range(0,X):
    subject_list.append(list(map(float, raw_input().split())))

for i in range(0,N):
    student = zip(*subject_list)
    marks = 0.0
    for j in range(0,X):
        marks = marks + student[i][j]
        avg = marks/X
    print(avg)
