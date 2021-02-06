# randomfruit.py
# A program that selects a random object from a list
# Author: Fiachra O' Donoghue

import random


# Create list of fruit
fruits = ['apple', 'banana', 'plum', 'pineapple', 'melon', 'lemon', 'orange', 'pomegranate']

# Create a tuple of fruit
fruits2 = ('apple', 'banana', 'plum', 'pineapple', 'melon', 'lemon', 'orange', 'pomegranate')

# randomly select a fruit using the the choice method of the random module
fruit = random.choice(fruits)

# randomly select a fruit using the randint method
fruit2 = fruits2[random.randint(1, len(fruits2) - 1)]

# inform user of choice
print("My favourite fruit:", fruit)

# or maybe...
print("or maybe it's:", fruit2)