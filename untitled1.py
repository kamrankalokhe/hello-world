#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 07:05:24 2018

@author: kkalokhe
"""

import unittest

#(n)
def isUnique(string):
    
    if len(string)>128:
        return False
    
    char_set = [False for _ in range(128)]
    print("Char Set=", char_set)
    for char in string:
        val = ord(char)
        print("value=", val)
        
        if char_set[val]:
            
            #char already found in string
            
            return False
        char_set[val] = True
        print("char_Set", char_set)
        
    return True


x = unique('abcd')

