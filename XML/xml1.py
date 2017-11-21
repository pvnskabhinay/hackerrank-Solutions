#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:10:32 2017

@author: venkatapochiraju
"""

def get_attr_number(node):
    score = 0
    for e in node.iter():
        score += len(e.attrib)
    return score
