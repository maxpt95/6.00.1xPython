# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:37:40 2021

@author: maxpe
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    assert type(s) == str, "Input most be a string"
    
    noVowelS = ""
    
    for i in range(len(s)):
        if s[i] not in "aeiouAEUIOU" :
            noVowelS += s[i]
    
    print(s)
    print(noVowelS)

print_without_vowels("Hello, Max. How are you?")
print_without_vowels("aeiou")
print_without_vowels("HEllo, Max. aeou How are you?")