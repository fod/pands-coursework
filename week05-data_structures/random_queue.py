# random_queue.py
# Create a queue of random numbers and empty it
# Author: Fiachra O' Donoghue

# Import the randint function to produce random integers
from random import randint

# Generate a list of 10 random numbers between 1 and 100 using a list comprehension
random = [ randint(1,101) for i in range(10) ]

# Print the list
print("queue is {}".format(random))

# Continue looping until the list is empty
while len(random) > 0:

    # Print the popped first number from the list and the remaining list
    print("current number is {} and the queue is {}".format(random.pop(0), random))

# Print the empty queue message
print("the queue is now empty")