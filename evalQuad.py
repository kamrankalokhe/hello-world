#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:12:39 2018

@author: kkalokhe
"""

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here 
    q1 = evalQuadratic(a1, b1, c1, x1)
    q2 = evalQuadratic(a2, b2, c2, x2)
    
    return (q1+q2)


print (twoQuadratics(-1.04, -8.36, -2.59, 6.07, -3.99, 6.31, -4.83, 0.42))