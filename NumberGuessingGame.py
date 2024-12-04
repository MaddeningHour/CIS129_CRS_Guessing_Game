#Christopher Robles Serrano
#Number guessing game extra credit
#12/3/24
#This program is a guessing game between two values.

#Importing random to generate a random winning number
from random import *


def validvariable(lowRange=0,highRange=10000):
    #Looping over until myGuess is valid
    while True:
        #Receiving input from user between our minumum/maximum and removing white space.
        myGuess = input(f"\nEnter a number between {lowRange}-{highRange}: ").strip()
        
        #Trying to convert to integer and returning
        try:
            myGuess = int(myGuess)
            return myGuess
        
        #If failed print error statement and loop back to top
        except ValueError:
            print("Invalid input!")
       

def game():
    #Our ranges and winning number.
    MIN = 0
    MAX = 10000
    WIN_NUM = randint(0,10000)

    #The comment underneath this one can be uncommented for testing.
    #print(WIN_NUM)

    print(f'Welcome to my numbers guessing game!')
    #Method call passing in our minimum and maximum
    myguess = validvariable(MIN,MAX)

    #Counter to keep track of number of valid attempts.
    counter = 1
    
    #Sentinel based logic. As long as the user guess is WIN_NUM the program keeps looping.
    while myguess != WIN_NUM:
        
        #If the guess is outside of the valid ranges it'll keep looping until a valid number is input.
        while (myguess < MIN) or (myguess > MAX):
            print(f'Error! Guess must be between {MIN}-{MAX}\n')
            myguess = validvariable(MIN,MAX)

        #If the user input is greater than the winning number the new maximum value is that input.
        if myguess > WIN_NUM:
            print('Too high! Try again!')
            MAX = myguess
        
        #Else if the user input is smaller than the winning number the new minimum value is that input.
        elif myguess < WIN_NUM:
            print('Too low! Try again!')
            MIN = myguess
        
        #Incrementing counter to keep track of attempts
        counter += 1

        #New guess to before the loops starts over.
        myguess = validvariable(MIN,MAX)
    
    #Print statements 
    print(f'WINNER! You guess the winning number: {WIN_NUM}\nIt took you {counter} attempt(s)')   
    
    #Checking if the user wants to play again. Converting to lowercase and stripping. 
    replay = input('Play again? (Yes or No)').lower().strip()
    while replay not in ['yes','no']:
        print('Invalid choice\n')
        replay = input('Play again? (Yes or No)').lower().strip()
    
    #Calling our game(main) method to start over again if wanted.
    if replay == 'yes':
        game()

    #Else the progam ends.
    else:
        print('Bye bye!')

#Main method call.
game()