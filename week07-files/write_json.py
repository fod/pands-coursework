# write_json.py
# Write a dict to a file
# Author: Fiachra O' Donoghue

import json

# Create a test dict
data = {"name": "John", "age": 42, "grades":[67,89,45,32,23,55]}

# Open a file for writing (create if it doesn't exist)
with open("json_write.txt", "w") as file:
    json.dump(data, file)


    