# isEven.py
# A program which informs the user whether an entered number is even or odd
# Author: Fiachra O' Donoghue

# Declare num now so that it can be used as sentinel in while loop
num = 0

# Keep looping unitil num, which is where user input is stored, is set to -1
while (num != -1):

    # Number input is cast to an int as the concept of even and odd doesn't really 
    # apply to numbers with a non-zero fractional part
    num = int(input("Please enter an integer: "))

    # If the user has entered -1 then this is the final iteration of the loop 
    # so time to say goodbye
    if (num == -1):
        print("Goodbye")

    # If the number is evenly divisible by 2 then it is even
    # The modulus operator returns the remainder of a division operation 
    # ... therefore if num % 2 is equal to 0 then num is even
    elif (num % 2 == 0):

        # If the number is even print this message
        print("The number {} is even".format(num))
    else:
    
        # otherwise print this message
        print("Then number {} is odd".format(num))
