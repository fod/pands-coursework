# div.py
# A program that divides one user-provided number by another and prints the integer result and the remainder
# Author: Fiachra O' Donoghue

# Ask for the numbers and cast the inputted numbers from strng to int
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# Produce the integer result using the integer division (//) operator
intResult = num1 // num2

# Produce the remainder result using the modulo (%) operator
remainder = num1 % num2

# Print the result using the string format() method to interpolate results into the output string
print("The integer part of the result is: {} and the remainder is: {}".format(intResult, remainder))