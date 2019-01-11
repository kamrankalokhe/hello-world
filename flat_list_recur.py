#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 19:09:08 2018

@author: kkalokhe
"""
flat_list = []

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
        return []
    else:
        for index,elements in enumerate(aList):
            if isinstance(elements,list) and not isinstance(elements,(str,bytes)):
                flatten(elements)
            else:
                flat_list.append(elements)
                
    
    return flat_list
                

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

a = flatten(aList)
print(a)