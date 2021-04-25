# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 19:43:19 2021

@author: maxpe
"""

def f1():
    print("Inside f1");
def f2(x):
    print("Inside f2")
    return x;

f2(f1());