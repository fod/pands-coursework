# normalise.py
# A program that trims and lowercases input an informs 
# the user of the string length before and after normalisation
# Author: Fiachra O' Donoghue

inputString = input("Please enter some text: ")

# record pre normalisation length
beforeLength = len(inputString)

# Trim leading and trailing whitespace and make string lowercase
inputString = inputString.strip().lower()

# record post normalisation string length
afterlength = len(inputString)

# inform user of results
print("\nThe normalised string is {}.\nThe length of the string before "
      "normalisation was {} and the length after normalisation was {}.".
      format(inputString, beforeLength, afterlength))