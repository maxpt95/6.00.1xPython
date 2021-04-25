# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:41:27 2021

@author: maxpe
"""
print('Hello!');

inNum = int(input('Enter a Number: '));
for num in range(inNum,1,-2):
    print(num);
for num in range(2,inNum+1,2):
    print(num);

print('Goodbye!');

end = int(input('Enter a Number: '));
endSum = 0;
for end in range(end, 0, -1):
    endSum += end;
print(endSum);