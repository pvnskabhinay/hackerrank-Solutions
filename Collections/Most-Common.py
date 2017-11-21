#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:09:42 2017

@author: venkatapochiraju
"""

#!/bin/python3

import sys
from collections import Counter
if __name__ == "__main__":
    s = Counter(input().strip())
    most_common = sorted(s.items(), key = lambda x: (-x[1], x[0]))[:3]
    for c in most_common:
        print(*c[0], end = " ")
        print(str(c[1]), end = "\n")
