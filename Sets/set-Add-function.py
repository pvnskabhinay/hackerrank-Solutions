#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:43:00 2017

@author: venkatapochiraju
"""

n = int(input())
countries = set()
for i in range(n):
    countries.add(input())

tot_num = len(countries)
print(tot_num)
