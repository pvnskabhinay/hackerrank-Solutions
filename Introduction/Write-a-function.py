#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:27:47 2017

@author: venkatapochiraju
"""

def is_leap(year):
    leap = False
    if (year >=1900) & (year<=100000):
        if ((year%4 == 0) & (year%100 != 0)) | (year%400 == 0) :
                leap = True
    return leap