#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:42:08 2018

@author: kkalokhe
"""

s  = "azcbobobegghakl"

maxsubstring = ""
temp =""
previouschar =""

for char in s:
    if char > previouschar:
        temp+= char
        if len(temp) > len(maxsubstring):
            maxsubstring = temp
        else:
            temp = char
        previouschar = char

print (maxsubstring)
            