# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:51:47 2021

@author: maxpe
"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    return sum(len(v) for v in aDict.values());

animals = { 'a': ['a','ardvark'], 'b': ['baboon'], 'c': ['coati']}
print(how_many(animals))
