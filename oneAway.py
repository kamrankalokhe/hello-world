#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:48:24 2018

@author: kkalokhe
"""

def oneAway(s1,s2):
    
    sum = 0
    
    for char in s1:
        if char in s2:
            continue
        else:
            sum +=1
            
    if sum > 1:
        return False
    else:
        return True


print(oneAway("pale","ple"))
print(oneAway("pales","pale"))
print(oneAway("pale","bale"))
print(oneAway("pale","bake"))

    
    
    
    
    