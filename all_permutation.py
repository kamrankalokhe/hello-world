#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:03:43 2018

@author: kkalokhe
"""

def permutation(word):
	if (len(word) <= 1):
		return [word]
	perms = permutation(word[1:])
	char = word[0]
	allPermutations = []
	for perm in perms:
		for i in range (len(perm)+1):
			allPermutations.append(perm[:i] + char + perm[i:])
	return allPermutations

print (permutation("abc"))