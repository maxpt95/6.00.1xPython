# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 07:49:30 2021

@author: maxperez
"""
x = int(input("Enter an Integer: "));
y = int(input("Enter an Integer: "));
z = int(input("Enter an Integer: "));

BiggestOddNumber = 0;
if y % 2 == 0 and x % 2 == 0 and z % 2 == 0:
    print("There are no odd numbers");
else:
    if y % 2 != 0:
        BiggestOddNumber = y;
    if x % 2 != 0 and  x > BiggestOddNumber:
        BiggestOddNumber = x;
    if z % 2 != 0 and z > BiggestOddNumber:
        BiggestOddNumber = z;
    print("Biggest odd number is: " + str(BiggestOddNumber));    