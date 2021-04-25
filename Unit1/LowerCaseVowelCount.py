# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:21:20 2021

@author: maxperezt

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
your program should print:
   
    Number of vowels: 5
"""

s = input('Enter a lower case string: ');

countVowel = 0;
for letter in str.lower(s):
    if letter in 'aeiou':
        countVowel += 1;
print('Number of vowels:',countVowel);