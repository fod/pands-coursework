# grade.py
# Convert an entered percentage mark to a grade
# Author: Fiachra O' Donoghue

# Variable must be initialised outside while loop so that it is available after loop ends
percentage = 0
grade = ""


# Flag indicating whether the input has been validatedas being within allowable range
validated = False

# Request for input is placed within a while loop so that the number input can be validated
# If the input value passes the validation check (must be between 0 and 100) then the 'validated'
# boolean variable is set to true and the loop ends. Otherwise an error message is displayed and
# the loop reiterates to ask again for a value from the user
while (validated == False):
    percentage = float(input("Please enter your percentage: "))
    if (percentage not in range(0,101)):
        print("\nPercentage must be between 0 and 100\n")
    else:
        validated = True

# An if-elif-else statement assigns a grade based on percentage value
if percentage >= 70:
    grade = "Distinction"
elif percentage >= 60:  # If the code reaches this point then percentage must be less than 70
    grade = "Merit 1"
elif percentage >= 50:  # If the code reaches this point then percentage must be less than 60
    grade = "Merit 2"
elif percentage >= 40:  # If the code reaches this point then percentage must be less than 50
    grade ="Pass"
else:
     grade = "Fail"     # If the code reaches this point then percentage must be less than 40


# Print the result
print(grade)