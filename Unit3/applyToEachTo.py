# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:14:56 2021

@author: maxpe
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, square, halve, abs], -3)

