# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:57:35 2021

@author: maxpe
"""

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    assert type(N) == int, "Input must be an integer"
    
    primes = [2]
    
    for i in range(3,N+1,2):
        j = 3
        
        while True:
            if j == i:
                primes.append(i)
                break
            elif i % j == 0:
                break
            j += 2
    
    return primes
