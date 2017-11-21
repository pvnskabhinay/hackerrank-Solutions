#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:43:58 2017

@author: venkatapochiraju
"""

n = input()
roll_nos_n = set(input().split())
b = input()
roll_nos_b = set(input().split())
set_union = roll_nos_n.union(roll_nos_b)
print(len(set_union))
