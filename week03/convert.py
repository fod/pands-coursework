# convert.py
# Program that takes a monetary value and returns its absolute value in cents
# Author: Fiachra O' Donoghue

amount = float(input("Please enter an amount in dollars: "))

# Convert to cents
amount *= 100

# Ensure amount is a positive integer
amount = int(abs(amount))

# Output result
print("You have {} cents".format(amount))