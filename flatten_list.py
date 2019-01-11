#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:58:35 2018

@author: kkalokhe
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flat_list = []
    if aList == []:
        return []
    else:
        for index, elements in enumerate(aList):
            if not isinstance(elements,list):
                flat_list.append(elements)
            else:
                    
                for nested_elements in elements:
                    flat_list.append(nested_elements)
    
    return (flat_list)
                
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

a = flatten(aList)
print(a)