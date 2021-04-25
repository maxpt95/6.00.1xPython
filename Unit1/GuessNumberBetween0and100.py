# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:53:21 2021

@author: maxperezt
"""

Epsilon = 0.01;
Low = 0;
High = 100;
Guess = (High + Low)/2;

print("Please think of a number between 0 and 100");


while abs(Guess - High) >= Epsilon:
    print("Is your secret number " + str(Guess) + "?");
    #print("Enter 'h' to indicate the guess is too high.", end=" ");
    #print("Enter 'l' to indicate the guess is too low.",end=" ");
    GuessReview = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ");
    
    if GuessReview == 'h':
        High = Guess;
    elif GuessReview == 'l':
        Low = Guess;
    elif GuessReview == 'c':
        break;
    else:
        print("Sorry I did not understand your input.");

    Guess = int((High + Low)/2);
    
print("Game over. Your secret number was:",Guess);