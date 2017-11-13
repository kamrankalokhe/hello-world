#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:40:37 2017

@author: kkalokhe
"""

s = 'azcbobobegghakl'

numVowel=0
for char in s:
    if char == 'a' or char == 'e'  or char == 'i' or \
    char == 'o' or char == 'u':
        numVowel +=1
        
print ("Number of vowels:" + " " + str(numVowel))