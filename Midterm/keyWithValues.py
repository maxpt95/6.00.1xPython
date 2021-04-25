# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:47:39 2021

@author: maxpe
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    targetKeys = []
    for key, value in aDict.items():
        if value == target:
            targetKeys.append(key)
    
    targetKeys.sort()
    return targetKeys

print(keysWithValue({8: 1, 1: 2, 9: 0, 0: 1, 7: 0}, 0))