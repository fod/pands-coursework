# average.py
# A program that accumulates a series of entered numbers anf outputs their average
# Author: Fiachra O' Donoghue

# Declare variable to hold current number
currentNum = None

# Declare a list to hold all of the entered numbers here so that it
# is available both within and after the while loop
numbers = []

# Accumulate numbers until a 0 is entered
while (currentNum != 0):

    # Numbers are cast as floats
    currentNum = float(input("Enter a number (0 to exit): "))

    # add  current number to the number list unless the current number is 0
    if currentNum != 0:
        numbers.append(currentNum)

# Print out the numbers
for number in numbers:
    print(number)

# Calculate the average
average = sum(numbers) / len(numbers)
print("Average: {}".format(average))