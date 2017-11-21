#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:11:11 2017

@author: venkatapochiraju
"""

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem) != 0:
        maxdepth = maxdepth+1
        for e in elem:
            level = level + 1
            maxdepth = max(depth(e,level+1),maxdepth)
