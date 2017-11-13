#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:34:24 2017

@author: kkalokhe
"""

#s = 'azcbobobegghakl'

#s= 'abcdefghijklmnopqrstuvwxyz'
s = 'lojjisxy'
substring=""
lstring = ""
prevchar =""
nextchar =""
for i in range(len(s)-1):
    
    if s[i] <= s[i+1]:
        char=s[i]
        nextchar = s[i+1]
        if char >= prevchar:
            substring += char
            prevchar = char
            print("if prechar " + prevchar + " char "+ char + " nextchar "+ nextchar)
        else:
            prevchar= ""
            
    else:
        nextchar= s[i]
        substring += nextchar
        if len(substring) > len(lstring):
            lstring = substring
        prevchar = ""
        substring= ""
        print("else prechar " + prevchar + " char "+ char + " nextchar "+ nextchar)
        
    if i+2  == len(s):
        substring += nextchar

if len(substring) > len(lstring):
    lstring = substring
print("Longest substring in alphabetical order is: " +lstring)
