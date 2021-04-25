# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:02:53 2021

@author: maxpe
"""
def gcditer(a,b):
    """
    a : integer >= 0
    b : integer >= 0
    Return greates common divisor
    """
    a, b = int(abs(a)), int(abs(b));
    if a > b:
        guess = b;
    else:
        guess = a;

    while (a % guess != 0 or b % guess != 0) and (guess  > 1):
        guess -= 1;
    
    return guess;

a = int(input("Enter an integer: "));
b = int(input("Enter a second integer: "));

gcd = gcditer(a, b);
print("The greatest common divisor of " + str(a) + " and " + str(b), end=" ")
print (" is: " + str(gcd));
