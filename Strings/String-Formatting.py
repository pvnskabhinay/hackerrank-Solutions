#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:39:05 2017

@author: venkatapochiraju
"""

def print_formatted(number):
    w = len('{:b}'.format(number))
    for i in range(1,number+1):
        print(str.rjust(str(i),w),str.rjust('{:o}'.format(i),w),str.rjust('{:X}'.format(i),w),str.rjust('{:b}'.format(i),w))
