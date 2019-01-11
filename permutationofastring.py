#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:58:58 2018

@author: kkalokhe
"""
'''
def isAPermutation(a_string, b_string):
	if len(a_string) != len(b_string): 
		print( "Not a Permutation")
	if sorted(a_string) == sorted(b_string): 
		print ("Is a Permutation")
	else:
		print( "Not a permutation")
isAPermutation("prashast", "rapshast")
'''



def isPermutation(a_string,b_string):
    if len(a_string) != len(b_string):
        print("not permutation")
    else:
        if sorted(a_string) == sorted(b_string):
            print("permutation")

isAPermutation("prashast", "rapshaqt")