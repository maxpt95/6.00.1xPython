# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:26:43 2021

@author: maxpe
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:14:04 2021

@author: maxpe

Write a iterative function iterPower(base, exp) that calculates the exponential  
baseexp  by simply using successive multiplication. For example, iterPower(base, exp)
should compute  baseexp  by multiplying base times itself exp times. Write
such a function below.

This function should take in two values - base can be a float or an integer;
exp will be an integer  ≥  0. It should return one numerical value. Your code
must be iterative - use of the ** operator is not allowed.
"""
def iterPower(base, exp):
    """
    base : int or float
    exp : int >= 0
    
    Returns the power of the base taking an exponential
    """
    pwr = base;
    if exp != 0:
        for exp in range(exp,1,-1):
            pwr *= base;
        return pwr;
    else:
        return 1;

exp = abs(int(input("Enter an integer for your exponential: ")));
base = float(input("Enter a number to power up: "))

pwr = iterPower(base,exp);
print("The " + str(exp) +"º power of " + str(base) + " is = " + str(pwr));