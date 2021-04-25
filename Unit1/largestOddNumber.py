# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:49:14 2021

@author: maxpe
"""
largestOddNumber = None;
for i in range(10):
    number = int(input("Enter an integer: "));
    
    if (number % 2 != 0) and (largestOddNumber is None or largestOddNumber < number):
        largestOddNumber = number;
    
if largestOddNumber is None:
    print("No odd numbers where entered.")
else:
    print("The largest odd number entered is:" + str(largestOddNumber));