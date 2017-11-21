#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:27:16 2017

@author: venkatapochiraju
"""

if __name__ == '__main__':
    n = int(input())
    if (n>=1) & (n<=20):
        for i in range(0,n,1):
            print(i**2)