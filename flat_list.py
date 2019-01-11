#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:52:29 2018

@author: kkalokhe
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    key_list = []
    if aDict == {}:
        return []
    else:
        for k,v in aDict.items():
            if v == target:
                key_list.append(k)
            
        key_list.sort()
    
    return key_list
                
                
            
            