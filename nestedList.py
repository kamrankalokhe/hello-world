#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:20:33 2018

@author: kkalokhe
"""

def get_all_substrings(input_string):
    length = len(input_string)
    alist = []
    
    for i in range(length):
        for j in range(i,length):
            alist.append(input_string[i:j+1])
    return alist
    

print( get_all_substrings("abcd"))


def get_all_substring(string):
    length = len(string)
    return [string[i:j+1] for i in range(length) for j in range(i,length)]

print get_all_substrings("abcd")

