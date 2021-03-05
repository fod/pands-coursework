# studentMan_addStudents.py
# Developing the add student functionality for studentMan
# Author: Fiachra O' Donoghue

# Declare list to hold the students
# This list can be passed to doAdd and doView
students = []

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
        if enterMod == "y":
            modules.append(getModule())

        # otherwise construct a dict from the students name and list of module dicts
        else:
            studentList.append({"name": name, "modules": modules})

            # and break out of the add module loop
            break

    # return a reference to the studentlist to the caller
    return studentList


# The getModule function
# ... asks the user to enter a module and a grade and returns a single key-value dict 
# with the module as the key and the grade as the value
def getModule():

    module = input("Module: ")
    grade = input("Grade: ")

    return {module: grade}


# Test the functions
doAdd(students)
print(students)