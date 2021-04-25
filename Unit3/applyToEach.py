# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:03:06 2021

@author: maxpe
"""

def applyToEach(L, f):
    clone = L[:]
    for i in range(len(L)):
        clone[i] = f(clone[i]);
    print(clone);

testList = [1, -4, 8, -9];

applyToEach(testList, abs);

def Plus1(x):
    return x + 1;

applyToEach(testList, Plus1);

def pow2(x):
    return x * x;

applyToEach(testList, pow2);