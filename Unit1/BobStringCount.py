# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:42:23 2021

@author: maxperezt
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = input('Enter a lower case string: ');

s = str.lower(s)
countBob = 0;
for i in range(2, len(s), 1):
    if s[i] == 'b':
        isBob = s[i-2] + s[i-1] + s[i];
        if isBob == 'bob':
            countBob += 1;
            
print('Number of times bob occurs is:',countBob);

