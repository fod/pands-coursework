# isEven.py
# A program which informs the user whether an entered number is even or odd
# Author: Fiachra O' Donoghue

# Number input is cast to an int as the concept of even and odd doesn't really 
# apply to numbers with a non-zero fractional part
num = int(input("Please enter an integer: "))

# If the number is evenly divisible by 2 then it is even
# The modulus operator returns the remainder of a division operation 
# ... therefore if num % 2 is equal to 0 then num is even
if (num % 2 == 0):

    # If the number is even print this message
    print("The number {} is even".format(num))
else:
    
    # otherwise print this message
    print("Then number {} is odd".format(num))
