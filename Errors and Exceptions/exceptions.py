#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:07:34 2017

@author: venkatapochiraju
"""

T = int(input())
for i in range(T):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print ("Error Code: " + str(e))
    except ValueError as e:
        print ("Error Code: " + str(e))
