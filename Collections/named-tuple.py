#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:07:42 2017

@author: venkatapochiraju
"""

import collections
import statistics
N = int(input())
Student = collections.namedtuple('Student', input().split())
sum = 0
for i in range(N):
    line3input = input().split()
    student1 = Student(*line3input)
    sum = sum + int(student1.MARKS)
avg = sum/N
print(avg)
