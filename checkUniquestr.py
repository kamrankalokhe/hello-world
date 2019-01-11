#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:40:30 2018

@author: kkalokhe
"""

def luckySeven(numbers):
    length = len(numbers)
    for i in range(length - 2):
        list1 = numbers[i:i+3]
        if sum(list1) == 7:
            print "OK"


luckySeven([1,2,3,4,1,2])