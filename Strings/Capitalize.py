#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:40:02 2017

@author: venkatapochiraju
"""

def capitalize(string):
    lst = list(string)
    lst[0]=lst[0].upper()
    for i in range(1,len(lst)):
        if lst[i-1]==" ":
            lst[i]=lst[i].upper()
    string =  "".join(lst)
    return string
