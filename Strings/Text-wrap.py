#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:38:10 2017

@author: venkatapochiraju
"""

def wrap(string, max_width):
    string = (textwrap.fill(string,max_width))
    return string
