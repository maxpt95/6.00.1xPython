# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:10:18 2021

@author: maxpe
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        c = a;
        a = b;
        b = c;
  
    if a % b == 0:
        return b;
    else:
        return gcdRecur(b, a % b);
    
a = int(input("Enter an integer > 0: "));
b = int(input("Enter an integer > 0: "));

print(gcdRecur(a, b));