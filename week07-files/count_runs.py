# count_runs.py
# A program that records the number of times it has been run
# Author: Fiachra O' Donoghue

# Location of the file that stores the count of programme runs
countFile = "count.txt"
count = 0

# Read current value from countFile
with open(countFile) as file:
    count = int(file.read())

# Increment the count
count += 1

# Open the file for writing
with open(countFile, "w") as file:

    # Write the new run count to the file
    file.write(str(count))

