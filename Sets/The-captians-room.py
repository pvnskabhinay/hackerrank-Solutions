#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:45:49 2017

@author: venkatapochiraju
"""

K = int(input())
elements = list(map(int, input().split()))
elements_set = set(elements)
sum_set = sum(elements_set)
sum_elements = sum(elements)
Cap_room = (sum_set*K - sum_elements)//(K-1)
print(Cap_room)
