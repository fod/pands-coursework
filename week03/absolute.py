# absolute.py
# print the absolute value of an input number
# Author: Fiachra O' Donoghue

# input number is cast to float so that any number will be valid input
num = float(input("Please enter a number: "))

# Get absolute value
absnum = abs(num)

print("The absolute value of {} is {}".format(num, absnum))