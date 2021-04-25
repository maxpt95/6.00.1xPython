# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:27:25 2021

@author: maxpe
"""
print('Hello!');

num = 10;
num = int(input('Enter a Number: '))
while num >= 2:
    print(num);
    num -= 2;
    
while num <= 10:
    print(num);
    num += 2;
print('Goodbye!\n');

end = int(input('Enter a Number: '))
endSum = 0;
while end > 0:
    endSum += end;
    end -= 1;
    
print (endSum);