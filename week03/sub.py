# sub.py
# A program that asks for two numbers then subtracts the second from the first
# Author: Fiachra O' Donoghue

# Ask user to enter 2 numbers
# Entered numbers are viewed as strings by Python so they are cast to ints using the int() function
firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

# An output string is assembled using the format() method to insert 
# the two number variables and the result of their subtraction 
print ("{} minus {} is {}".format(firstNum, secondNum, firstNum - secondNum))