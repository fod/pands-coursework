# student_dict.py
# Storing student details in a dictionary
# Author: Fiachra O' Donoghue

# Create a dictionary containing student information
# Personal details are in a sub-dictionary so that they can be accessed like:
# student["PerosnalDetails"]["Name"], etc
# and grades are in a list of dictionaries so that they can be iterated through easily
student = {"PersonalDetails": 
                {"Name": "Mary"},
            "Grades": [
                {"Course": "Programming", "Grade": 45},
                {"Course": "History", "Grade": 99 }
            ]
           }

# Print STudent's personal details
print("Student: {}".format(student["PersonalDetails"]["Name"]))

# Iterate through the "Grades" list and extract the course name and grade from each (dict) item
for course in student["Grades"]:
    print("\t{}: {}".format(course["Course"], course["Grade"]))
