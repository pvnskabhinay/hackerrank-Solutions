#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:40:34 2017

@author: venkatapochiraju
"""

def minion_game(string):
    score_k = 0
    score_s = 0
    if (len(string) > 0) & (len(string) <= 10**6):
        for i in range(len(string)):
            if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
                score_k = score_k + len(string) - i
            else: 
                score_s = score_s + len(string) - i

        if score_s > score_k:
            print("Stuart", end=" ")
            print(score_s)
        elif score_s < score_k:
            print("Kevin", end =" ")
            print(score_k)
        else:
            print("Draw")
