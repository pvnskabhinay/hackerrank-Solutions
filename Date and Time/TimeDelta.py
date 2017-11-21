#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:07:09 2017

@author: venkatapochiraju
"""

#!/bin/python3

import sys
from datetime import datetime
formatinp = "%a %d %b %Y %H:%M:%S %z"

def time_delta(t1, t2):
    delta = int(abs(t1 - t2).total_seconds())
    return delta

    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = datetime.strptime(input(), formatinp)
        t2 = datetime.strptime(input(), formatinp)
        delta = time_delta(t1, t2)
        print(delta)
