#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:11:28 2017

@author: venkatapochiraju
"""

#!/bin/python3
import sys
def kangaroo(x1, v1, x2, v2):
    if (v2 < v1): 
        if((x2 - x1) % (v2 - v1)) == 0:
	        return("YES")
        else:
            return("NO")
    else:
	    return("NO")
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
