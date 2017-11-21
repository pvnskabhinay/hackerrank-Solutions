#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:32:58 2017

@author: venkatapochiraju
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = []
    for e in arr:
        lst.append(e)
    lst.sort()
    length = len(lst)
    max = lst[length-1]
    while lst[length-1] == max:
        lst.remove(max)
        length -=1
    print(lst[length-1])
