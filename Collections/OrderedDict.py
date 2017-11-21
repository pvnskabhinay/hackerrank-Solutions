#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:08:03 2017

@author: venkatapochiraju
"""

from collections import OrderedDict
items_input = list()
N = int(input())
for i in range(N):
    inp = input().strip().split()
    name = (" ").join(inp[0:len(inp)-1])
    price = int(inp[len(inp)-1])
    items_input.append((name, price))

d = OrderedDict()
for i in items_input:
    try:
        d[i[0]] += i[1]
    except KeyError as e:
        d[i[0]] = i[1]

for i in d.items():
    print (i[0], i[1])
