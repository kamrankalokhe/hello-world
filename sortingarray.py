#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:46:08 2018

@author: kkalokhe
"""

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]

new_list = []

minimum = data_list[0]

for x in len(data_list):
    #print("X= ",x)
    if x > minimum:
        continue
    else:
        (data_list[x], minimum)= (minimum,data_list[x])
        
        
    
    #new_list.append(minimum)
    #data_list.remove(minimum)
    


#print(new_list)
print(data_list)   
    
        