# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:02:30 2021

@author: maxpe
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    if aList == []:
        return aList;    
    else:   
        flatList = []
        for i, value in enumerate(aList):
            #if the value is a list then we need to flatten it and add it to our list
            if isinstance(value, list):
                flatList.extend(flatten(value))
            else:
                flatList.append(value)
            
        return flatList

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatList = flatten(L)
print(flatList)