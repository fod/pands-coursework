# guess1.py
# Guessing game: ask the user to guess a number repeatedly until the correct number is guessed
# Author: Fiachra O' Donoghue

# Import the random module which will provide randint, a method that generates random integers
import random

# Generate a random integer from 1 (inclusive) to 20 (exclusive)
secretNumber = random.randint(1,20)

# while(True) loops forever
while (True):

    # Ask user for their guess and store it in the 'guess' variable
    guess = int(input("I'm thinking of a number between 1 and 20. Can you guess it? "))


    # Compare the user's guess with the randomly generated secret number
    # If the guess is correct...
    if (guess == secretNumber):

        # Print a congratulatory message and break out of the infinite while loop
        print("Well done - you got it!")
        break

    # Otherwise print a commiserative message 
    # and allow the infinite while loop to enter another iteration
    else:
        print("Sorry. Try again.")