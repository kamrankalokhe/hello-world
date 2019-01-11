#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:04:20 2018

@author: kkalokhe
"""

def is_palin_perm(string):
    
    string = string.replace(" ","")
    string = string.lower()
    
    d= dict()
    
    for char in string:
        if char in d:
            d[char] +=1
        else:
            d[char] =1
    
    odd_count = 0
    
    for k,v in d.items():
        if v%2 !=0 and odd_count == 0:
            odd_count +=1
        elif v%2 !=0 and odd_count !=0:
            return False
    
    return True

print(is_palin_perm(string="racecar"))

print(is_palin_perm(string="This is  a car"))

        
    