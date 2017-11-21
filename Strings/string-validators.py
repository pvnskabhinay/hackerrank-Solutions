#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:37:22 2017

@author: venkatapochiraju
"""

if __name__ == '__main__':
    s = input()
    if len(s)>0 & len(s)<1000:
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isdigit() for c in s))   
        print(any(c.islower() for c in s))
        print(any(c.isupper() for c in s)) 
    else:
        sys.exit()
