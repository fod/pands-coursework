# guess2.py
# Guessing game: ask the user to guess a number repeatedly until the correct number is guessed
# Inform the user on each guess whether their guess is higher or lower than the answer
# This solution will use a different form of the while loop than guess1.py      
# Author: Fiachra O' Donoghue

# Import the random module which will provide randint, a method that generates random integers
import random

# Generate a random integer from 1 (inclusive) to 20 (exclusive)
secretNumber = random.randint(1,20)

# declare guess outside the while loop so that it's available in the loop's termination condition
guess = 0

# Keep looping until the guess matches the secret number
while (guess != secretNumber):

    # Ask for the user's guess and cast it to an int
    guess = int(input("I'm thinking of a number between 1 and 20. Can you guess it? "))

    # Compare the guess to the secret number and if they don't match 
    # print out an indicative message
    if guess < secretNumber:
        print("Too low!")
    elif guess > secretNumber:
        print("Too high!")

# If the code reaches this point then the guess must have matched the secret number
# and therefore fulfille the termination condition of the loop
# Print a congratulatory message
print("Well done! The number was {}.".format(secretNumber))