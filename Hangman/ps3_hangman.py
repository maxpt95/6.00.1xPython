# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = True;
    i = 0;
    while i < len(secretWord) and guessed:
        guessed = secretWord[i] in lettersGuessed;
        i += 1;
    
    return guessed; 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    for letter in secretWord:
        if letter not in lettersGuessed and letter != '_ ':
            secretWord = secretWord.replace(letter, '_ ')
    
    return secretWord;

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #initially all lowercase letters will be available
    availableLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '');
    
    return availableLetters

def askGuess(guessesLeft, availableLetters):
    '''
    asks the player to guess a letter from the secret word
    guessLeft: int, the number of tries the player has to guess 
        the secret word
    availableLetters: list, all letters available for the playe to guess from
    returns: string, letters Guessed by the player;
    '''
    print("You have " + str(guessesLeft) + " guesses left.");
    print("Available letters: "+ availableLetters);
    
    return input("Please guess a letter: ");

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!");
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.");
    print("-------------");
    
    #now we let the player guess what word we picked 
    guessesLeft = 8;
    lettersGuessed = []; 
    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        availableLetters = getAvailableLetters(lettersGuessed)
        guess = askGuess(guessesLeft, availableLetters);
        
        #we provide feedback if its a repeated, wrong or right guess.
        if guess not in availableLetters:
            feedback = "Oops! You've already guessed that letter: ";
        
        elif guess not in secretWord:
            lettersGuessed.append(guess);
            feedback = "Oops! That letter is not in my word: ";
            guessesLeft -= 1;
        
        else:
            lettersGuessed.append(guess);
            feedback = "Good guess: ";

        print(feedback + getGuessedWord(secretWord, lettersGuessed));
        print("-------------");
        
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!");
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

secretWord = chooseWord(wordlist).lower();
hangman(secretWord);




