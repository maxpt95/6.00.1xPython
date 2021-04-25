# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:15:27 2021

@author: maxpe
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    aStr = str.lower("".join(sorted(aStr)));
    if aStr and char == aStr[0]:
        return True;
    elif len(aStr) <= 1:
        return False;
    else:
        return isIn(char,aStr[1:])

aStr = input("Enter a String: ");
char = input("Entar a letter to look for in the string: ")
if isIn(char,aStr):
    print("The letter " + char + " has been found in " + aStr);
else:
    print("The letter " + char + " does not exist in "+ aStr);