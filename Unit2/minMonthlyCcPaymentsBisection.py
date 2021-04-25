# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 07:24:41 2021

@author: maxpe
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:06:18 2021

@author: maxperezt
Calculate the minimum fixed monthly payments needed to pay off a credit card
give:
    balance
    Annual Interest Rate
"""

balance = int(input("Enter your present balance: "));
annualInterestRate = float(input("Enter your annual interest rate: "));


timePeriod = 12;
lowPayment = balance/timePeriod;

monthlyInterestRate = annualInterestRate / timePeriod
highPayment = (balance * ( 1 + monthlyInterestRate)**timePeriod)  / timePeriod;

fixedMonthlyPayment = (lowPayment + highPayment)/2;
remainingBalance = balance;
epsilon = 0.12;
while abs(remainingBalance) >= epsilon:
    
    remainingBalance = balance;
    #If a year has passed and the balance hasn't being paid we start over.
    for i in range(timePeriod):
        monthlyUnpaidBalance = remainingBalance - fixedMonthlyPayment;
        remainingBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate);

    if remainingBalance < -epsilon:
        highPayment += remainingBalance/12;
    elif remainingBalance > epsilon:
        lowPayment += remainingBalance/12;
        
    fixedMonthlyPayment = (lowPayment + highPayment)/2;

print("Lowest Payment: " + str(round(fixedMonthlyPayment,2)));