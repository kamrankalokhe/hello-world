#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:37:21 2018

@author: kkalokhe
"""

def stringCompression(s):
    length = len(s)
    cs = ""
    count = 1
    cs += s[0]
    
    for i in range(length-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            
            if (count >=1):
                cs += str(count)
            cs += s[i+1]
            count =1
            
    if count>=1 :
        cs +=str(count)
    
    
    print(cs)


stringCompression("abbccccd")         
            
    
	