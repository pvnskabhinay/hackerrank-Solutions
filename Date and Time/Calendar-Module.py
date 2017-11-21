#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:06:41 2017

@author: venkatapochiraju
"""

import calendar
m,d,y = map(int, input().split())
if y>2000 and y<3000:
    print(calendar.day_name[calendar.weekday(y, m, d)].upper())
