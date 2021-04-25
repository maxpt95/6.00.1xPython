# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:06:18 2021

@author: maxperezt
Calculate the minimum fixed monthly payments needed to pay off a credit card
give:
    balance
    Annual Interest Rate
"""
def remainingCreditCardBalance(balance, annualInterestRate, fixedMonthlyPayment, 
                               timePeriod = 12):
    """
    Parameters
    ----------
    balance (int or float): current credit card balance
    annualInterestRate (float): has to be between 0 and 1
    timePeriod (int) optional: number of months default is 12
    fixedMonthlyPayment (int): multiple of 10. It will check if this payment is enough
    to pay the balance.
    
    Returns
    -------
    monthlyPayment (int): it will be a multiple of 10
    """
    if timePeriod == 0:
        return balance;
    else:
        monthlyInterestRate = annualInterestRate / 12;
        monthlyUnpaidBalance = balance - fixedMonthlyPayment;
        
        #lastly we calculate our monthtly balance.
        balance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate);
        
        return remainingCreditCardBalance(balance, annualInterestRate, 
                                          fixedMonthlyPayment, timePeriod - 1)

balance = int(input("Enter your present balance: "));
annualInterestRate = float(input("Enter your annual interest rate: "));

fixedMonthlyPayment = 10;
remainingBalance = balance;

while remainingBalance > 0:
    remainingBalance = balance;
    
    remainingBalance = remainingCreditCardBalance(balance, annualInterestRate, 
                                                 fixedMonthlyPayment);
    
    fixedMonthlyPayment += 10;

print("Lowest Payment: " + str(fixedMonthlyPayment - 10));