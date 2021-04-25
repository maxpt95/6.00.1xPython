# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 09:22:49 2021

@author: maxpe
"""

def addNumbersInStr(s):
    """
    s : string
        A sequence of floats or integers separated by a ,
    Returns float
        The total sum of all the numbers
    """
    total = 0;
    exStrNum = "";
    for i in range(len(s)):
        if s[i] == ",":
            total += float(exStrNum);
            exStrNum = "";
        else:
            exStrNum += s[i];
    
    total += float(exStrNum);#adding the last number of s
    return total;

s = input("Enter a sequence of floats separated by a ',': ");
total = addNumbersInStr(s);

print("The sum of all your numbers is: " + str(total));