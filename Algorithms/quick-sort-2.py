#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:14:30 2017

@author: venkatapochiraju
"""

def quickSort(ar):
    if len(ar) is 0:
        return ar
    p = 0
    for i in range(len(ar)):
        if ar[i] < ar[p]:
            ar = ar[0:p] + [ar[i]] + ar[p:i] + ar[i+1:]
            #print(*ar)
            p += 1
    if p < 2:
        if len(ar) - p < 3:
            if len(ar) > 1:
                print (*ar)
            return ar
    result =  quickSort(ar[0:p]) + [ar[p]] + quickSort(ar[p+1:])
    print (*result)
    return result

n = int(input())
ar = list(map(int,input().split()))
p = ar[0]
quickSort(ar)
