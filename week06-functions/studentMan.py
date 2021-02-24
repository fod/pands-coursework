# studentMan.py
# A student management program
# Author: Fiachra O' Donoghue

# Create the menu
def menu():

    # Print out menu
    print("\nWhat would you like to do?\n", \
    "\t(a) Add a new student\n", \
    "\t(v) View students\n", \
    "\t(q) Quit\n")

    # Get user input and place in 'selection' variable
    selection = input("Type one letter (a/v/q): ")

    # Echo selection value to user
    print("You chose", selection)


# call function
menu()