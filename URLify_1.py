#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 07:50:04 2018

@author: kkalokhe
"""

def URLify(string):
    
    new_str = ""
    
    for char in string:
        if char != " ":
            new_str += char
        else:
            new_str += '%20'
    
    return(new_str)
    

string = "Mr John Smith"  
print(URLify(string))
                