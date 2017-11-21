#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:36:54 2017

@author: venkatapochiraju
"""

def count_substring(string, sub_string):
    no_of_occ = 0
    if len(string) >=1 & len(string)<=200:
        for i in range(0, len(string)):
            if(string[i:].startswith(sub_string)):
                no_of_occ +=1
    return no_of_occ
