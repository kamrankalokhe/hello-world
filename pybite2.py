#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:31:59 2018

@author: kkalokhe
"""

VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        color = input('Enter color:')
        color = color.lower()
        if color == 'quit':
            print('bye')
        break
    
        if color not in VALID_COLORS:
            print('Not a valid color')
            continue
        else:
            print(color)
    