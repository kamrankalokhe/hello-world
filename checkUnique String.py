#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 20:29:30 2018

@author: kkalokhe
"""

def unique(s):
    uchar = ""
    for char in s:
        if char not in uchar:
            uchar += char
        else:
            continue
    if len(uchar) == len(s):
        print("Unique")
        print(uchar)
    else:
        print("Not unique")
    
    
    
unique("kamran")
    
        