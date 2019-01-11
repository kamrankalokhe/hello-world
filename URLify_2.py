#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 08:17:27 2018

@author: kkalokhe
"""

def URLify(string,length):
    
    new_index = len(string)
    
    for i in reversed(range(length)):
        
        if string[i] == " ":
            string[new_index-3 :new_index] = "%20"
            
        
        
        
        
    
    

string = "Mr John Smith  "  
 
length =13
URLify(string,length)