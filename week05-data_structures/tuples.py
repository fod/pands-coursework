# tuples.py
# Representing the months of the year with tuples       
# Author: Fiachra O' Donoghue

# Create a tuple holding the names of the months as strings
year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Subset the tuple to just get the summer months
summer = year[4:7]

# Iterate through summer tuple and print each value
for month in summer:
    print(month)