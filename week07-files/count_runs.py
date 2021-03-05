# count_runs.py
# A program that records the number of times it has been run
# Author: Fiachra O' Donoghue

# Count-reading function
def readCount(filename):

    # Read current value from countFile
    with open(filename, "r") as file:
        count = int(file.read())

        # return count to caller
        return count


# Count-writing function
def writeCount(filename, count):

    # Open the file for writing
    with open(filename, "w") as file:

        # Write the new run count to the file
        file.write(str(count))


# Location of the file that stores the count of programme runs
countFile = "count.txt"

# Read the current dount from the count file
count = readCount(countFile)

# Increment the count
count += 1

# Write out the new count
writeCount(countFile, count)





