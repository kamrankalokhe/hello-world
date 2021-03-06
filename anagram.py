#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 07:30:34 2018

@author: kkalokhe
"""

def is_anagram(s1,s2):
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] =1
    
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
        else:
            return True


print(is_anagram('anagram','nagaram'))
print(is_anagram('cat','rat'))

#Solution using collection

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
