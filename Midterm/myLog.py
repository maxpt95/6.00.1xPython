# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:01:04 2021

@author: maxpe
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    
    if b > x:
        return 0;
    elif b**2 > x:
        return 1;
    else:
        return myLog(x // b, b) + 1;
    
print(myLog(2, 2))