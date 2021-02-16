# student_dict.py
# Storing student details in a dictionary
# Author: Fiachra O' Donoghue

# Create a dictionary containing student information
student = {"Name": "Mary", "Programming": 45, "History": 99}


for k, v in student.items():
    print("{}: {}".format(k, v))