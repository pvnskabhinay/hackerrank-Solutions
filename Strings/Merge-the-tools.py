#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:41:06 2017

@author: venkatapochiraju
"""

def merge_the_tools(string, k):
    # your code goes here
    len_part = int(len(string)/k)
    for i in range (len_part):
        temp = ""
        for char in string[i*k:(i+1)*k]:
            if char not in temp:
                temp = temp + char
        print(temp)
