#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:33:44 2017

@author: venkatapochiraju
"""


if __name__ == '__main__':
    N = int(input())
    students = []
    for i in range(N):
        temp = []
        name = input()
        score = float(input())
        temp.append(name)
        temp.append(score)
        students.append(temp)
    
    x = []
    length = len(students)
    for i in range(length):
        x.append(students[i][1])
    min_x = min(x)
    
    y = []
    for i in range(length):
        if min_x != x[i]:
            y.append(x[i])
    min_y = min(y)
    
    student = []
    for i in range(length):
        if min_y == students[i][1]:
            student.append(students[i][0])
    student.sort()
    length_s = len(student)
    for i in range(length_s):
        print(student[i])
