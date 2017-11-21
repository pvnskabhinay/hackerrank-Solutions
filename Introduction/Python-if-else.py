#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:24:04 2017

@author: venkatapochiraju
"""

if __name__ == '__main__':
    n = int(input())
    if n%2 != 0:
        print ("Weird")
    else:
        if(n>=2) & (n<=5):
            print("Not Weird")
        elif (n>=6) & (n<=20):
            print("Weird")
        else:
            print("Not Weird")