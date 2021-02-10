# topthree.py
# Generate 10 random numbers and print out top 3
# Author: Fiachra O' Donoghue

# import the randint method from the random module
from random import randint

# Generate 10 random numbers in a for loop
numbers = []
for i in range(0,10):
    numbers.append(randint(1,101))

# Sort the list of numbers
numbers.sort()

# Print out the top 3 - i.e. the last three in the sorted list
for number in range(len(numbers) - 3, len(numbers)):
    print(numbers[number])