# studentMan2.py
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

    # Return users selection from function
    return selection

def doAdd():
    print("In adding...")

def doView():
    print("In viewing...")

while (True):
    selection = menu()

    if selection == "a":
        doAdd()
        continue
    elif selection == "v":
        doView()
        continue
    elif selection == "q":
        break
    else:
        continue
    
