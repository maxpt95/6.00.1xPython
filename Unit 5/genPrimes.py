# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:35:04 2021

@author: maxpe
"""

def genPrimes():
    prime = 2
    i = 2
    while True:
        if prime % i == 0:
            if i != prime:
                i = 1
                prime += 1
            else:
                yield prime
                i = 1
                prime += 1
        i += 1
          
primes = genPrimes()
for i in range(15):
   print(next(primes))
