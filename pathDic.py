#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:13:27 2018

@author: kkalokhe
"""

def print_directory_contents(sPath):
    import os
    print("List dir=",os.listdir(sPath))
    print("++++++++++++++++++++++++++")
    for sChild in os.listdir(sPath):
        
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
            

print_directory_contents("/Users/kkalokhe/Desktop/edX")