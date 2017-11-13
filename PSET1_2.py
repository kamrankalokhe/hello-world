#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:00:03 2017

@author: kkalokhe
"""

s = 'azcbobobegghakl'
mysum=0

for i in range(len(s)):
    #print(i)
    if s[i:i+3] == 'bob':
        mysum +=1


print("Number of times bob occurs is: " + str(mysum))


        
    
    
    
    
        
