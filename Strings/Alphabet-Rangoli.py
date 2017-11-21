#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:39:33 2017

@author: venkatapochiraju
"""

def print_rangoli(size):
    for i in range (-(size-1),size):
        for j in range (-2*(size-1),2*(size-1)+1):
            if j%2==0 and (abs(j//2)+abs(i))< size:
                  print (chr(abs(j//2)+abs(i)+ord('a')),end='')
            else:
                  print('-',end='')
        print()
