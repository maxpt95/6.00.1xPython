# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:12:30 2021

@author: maxpe

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
 
    Longest substring in alphabetical order is: beggh
 
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
    
    Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.
    
"""

s = input('Enter a lower case string: ');
s = str.lower(s)

index = 1;
OrderedStr, maxOrderedStr = s[0], s[0];

for letter in s[1:]:

        
    if (letter > s[index - 1] and letter not in OrderedStr) or (letter == s[index - 1]): #if previous letter is lower than present one
        OrderedStr += letter;
    else:
        OrderedStr = letter;
    
    if len(maxOrderedStr) < len(OrderedStr): #if it beats previous streak than I save it
        maxOrderedStr = OrderedStr;
    
    index += 1;
print(maxOrderedStr);