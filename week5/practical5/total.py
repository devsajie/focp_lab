import sys

# Determine how many elements are in sys.argv (script name + any args)
count = len(sys.argv)

# Initialise running total
total = 0.0

# Sum the numeric arguments (skip index 0 which is script name)
index = count - 1
while index > 0:
    total += float(sys.argv[index])
    index -= 1

# Number of numeric values passed
num_values = count - 1

# If there were any numeric arguments, compute and print total and average
if num_values > 0:
    average = total / num_values
    print("Total is", total)
    print("Average is", average)
else:
    # No numeric arguments were provided
    print("no arguments were provided")
