# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:22:37 2021

@author: maxpe
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    revL = []
    for subList in reversed(L):
        revSubList = list(reversed(subList))
        revL.append(revSubList)
    L[:] = revL

    
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print(L)
