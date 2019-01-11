#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:19:03 2018

@author: kkalokhe
"""

message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output"""
    message = message.split('\n')
    message = '|'.join(message)
    return(message)
    
print(split_in_columns(message=message))