#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 11:08:38 2018

@author: kkalokhe
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    
    return true
                    

    


secretWord = 'apple'       
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))  