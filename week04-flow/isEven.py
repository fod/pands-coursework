# isEven.py
# A program which informs the user whether an entered number is even or odd
# Author: Fiachra O' Donoghue

# Number input is cast to an int as the concept of even and odd doesn't really 
# apply to numbers with a non-zero fractional part
num = int(input("Please enter an integer: "))

if (num % 2 == 0):
    print("The number {} is even".format(num))
else:
    print("Then number {} is odd".format(num))
