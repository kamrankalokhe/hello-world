#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 15:45:47 2018

@author: kkalokhe
"""
import string

lowerstr = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lowerstr = string.ascii_lowercase
    value = ''
    str1 = ''
    for char in lowerstr:
        if char not in lettersGuessed:
            value = char
        else:
            value = ''
        str1 = str1 + value
        print(str1)
    return str1
            
    
   
            
            
  
            
        
    



lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))