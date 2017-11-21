#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:34:03 2017

@author: venkatapochiraju
"""

if __name__ == '__main__':
    from decimal import Decimal
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    avg = sum(student_marks[query_name])/3
    print "%.2f" %avg
