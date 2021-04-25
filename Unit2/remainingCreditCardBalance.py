# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:06:18 2021

@author: maxperezt
remainingCreditCardBalance (float): returns the remaining CC balance after a 
period of time.
"""

def remainingCreditCardBalance(balance, annualInterestRate, 
                               monthlyPaymentRate, timePeriod = 12):
    """
    Parameters
    ----------
    balance (int or float): the present balance owed.
    annualInterestRate (float)
    monthlyPaymentRate (float)
    timePeriod (int), optional: time period in months. The default is 12.

    Returns
    -------
    balance (float): the remaining balance after time period
    """
    if timePeriod == 0:
        return round(balance,2);
    else:
        minimumMonthlyPayment = monthlyPaymentRate * balance;
        monthlyUnpaidBalance = balance - minimumMonthlyPayment;
        monthlyInterestRate = annualInterestRate / 12;
        
        #lastly we calculate our monthtly balance.
        balance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate);
        
        return remainingCreditCardBalance(balance, annualInterestRate, 
                                          monthlyPaymentRate, timePeriod - 1)
    
balance = int(input("Enter your present balance: "));
annualInterestRate = float(input("Enter your annual interest rate: "));
monthlyPaymentRate = float(input("Enter your minimu montlhy paymente rate: "));

balance = remainingCreditCardBalance(balance, annualInterestRate, monthlyPaymentRate);

print("Remaining balance: " + str(balance));