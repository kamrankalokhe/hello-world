#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:34:04 2018

@author: kkalokhe
"""



def reverseWords(s):
    list1 = []
    s1 = s.split()
    len1= len(s1)
    for i in range(len1):
        s2 = s1[i][::-1]
        list1.append(s2)
    str1 = ' '.join(list1)
    print(str1)
reverseWords("Coding in Python")
    
    