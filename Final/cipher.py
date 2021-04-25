# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:14:51 2021

@author: maxpe
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    key_code = {map_from[i]:map_to[i] for i in range(len(map_from))}
    decoded = "".join([key_code[l] for l in code])
    
    return (key_code, decoded)

print(cipher("abcd", "dcba", "dab"))