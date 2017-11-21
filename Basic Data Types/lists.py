#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:29:10 2017

@author: venkatapochiraju
"""

if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(1,N+1,1):
        user_input = input().split()
        if user_input[0] == "insert":
            i = int(user_input[1])
            e = int(user_input[2])
            lst.insert(i,e)
        elif user_input[0] == "print":
            print (lst)
        elif user_input[0] == "remove":
            e = int(user_input[1])
            lst.remove(e)
        elif user_input[0] == "append":
            e = int(user_input[1])
            lst.append(e)
        elif user_input[0] == "sort":
            lst.sort()
        elif user_input[0] == "pop":
            lst.pop()
        elif user_input[0] == "reverse":
            lst.reverse()