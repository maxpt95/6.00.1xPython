# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:51:47 2021

@author: maxpe
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    key = None; #if its an empty dictionary we will return none.
    maxValue = max(aDict.values())
    
    for t in aDict.items():
        if len(maxValue) == len(t[1]):
            key = t[0];
    
    return key;

animals = { 'a': ['alpaca','ardvark'], 'b': ['baboon'], 'c': ['coati']};
print(biggest(animals));