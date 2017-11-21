#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:44:47 2017

@author: venkatapochiraju
"""

n = input()
roll_nos_n = set(input().split())
b = input()
roll_nos_b = set(input().split())
set_difference = roll_nos_n.difference(roll_nos_b)
print(len(set_difference))
