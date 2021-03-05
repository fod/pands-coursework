# read_json.py
# Read JSON from a file
# Author: Fiachra O' Donoghue

import json

datafile = "json_write.txt"

def readJSON(filename):
    # Open a file for writing (create if it doesn't exist)
    with open(filename, "r") as file:
        return json.load(file)

data = readJSON(datafile)

print(data)
