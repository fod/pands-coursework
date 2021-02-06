# floor.py
# Calculate and print out the floor of an input number
# Author: Fiachra O' Donoghue

import math

num = float(input("Please enter a number: "))

# Calculate floor
numFloor = math.floor(num)

print("The floor of {} is {}".format(num, numFloor))