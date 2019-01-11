#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:10:33 2018

@author: kkalokhe
"""

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)
print(type(games_won))


def print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    for k,v in games_won.items():
        print(k)
        print(v)
        if v == 1:
            print(f'{k} has won {v} game')
        else:
            print(f'{k} has won {v} games')
                
            
print_game_stats()