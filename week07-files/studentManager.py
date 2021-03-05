# studentManFinal.py
# The complete student manager
# Author: Fiachra O' Donoghue

studentList = []

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

def doAdd(studentList):

    # Declare a list to hold the module dicts
    modules = []

    # Get the student name
    name = input("\nName: ")

    # Infinite loop -- breaks when user declines to enter another module
    while(True):

        # Does the user have another modue to enter?
        enterMod = input("Do you wish to enter a module (y/n)? ")

        # if so, run the getModule function and add the resuting dict to the module list
        if enterMod.lower() == "y":
            modules.append(getModule())

        # if no more modules are to be entered construct a dict from 
        # the students name and list of module dicts
        elif enterMod.lower() == "n":
            studentList.append({"name": name, "modules": modules})
            
            # and break out of the add module loop
            break

        # if not y or n ask user again
        else:
            print("y or n please")
            next

    # return a reference to the studentlist to the caller
    return studentList


def getModule():

    module = input("Module: ")
    grade = input("Grade: ")

    return {module: grade}


def doView(studentList):
    print(studentList)


while (True):
    selection = menu()

    if selection == "a":
        doAdd(studentList)
        continue
    elif selection == "v":
        doView(studentList)
        continue
    elif selection == "q":
        break
    else:
        continue