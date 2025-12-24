import math

# PART 1: STRING FORMATTING

print("--- Part 1: String Formatting ---")

# Task: Basic Calculation
width = 104.32
height = 15.654
area = width * height
print(f"1. Basic: The area is {area}")

# Task: Precision (Decimal places)
print(f"2. Precision: The area is {area:.3f}")

# Task: Alignment and Padding
name = "Donald"
age = 75
print(f"3. Alignment: {name:$>20} - {age:$>20.2f}")

# Task: Circle Area with keyword argument
r = 52
circle_area = math.pi * r * r
print("4. Old Style Circle: Radius {} has area {area}".format(r, area=circle_area))

# [NEW] Task: Convert specific f-string to .format()
# The worksheet asks to convert: print(f"{name:@^15} - {age:#^10}")
print("5. Conversion Task: {name:@^15} - {age:#^10}".format(name=name, age=age))


 
# PART 2: FILE HANDLING
 
print("\n--- Part 2: File Handling ---")

# Task: Create and Write
print("6. Creating 'info.txt'...")
file_var = open("info.txt", "w") 
file_var.write("This is a text file\n")
file_var.write("It contains multiple lines of text\n")
file_var.write("This is the final line within the file\n")
file_var.close()

# Task: Read entire content
print("7. Reading entire file:")
file_var = open("info.txt", "r")
print(file_var.read())
file_var.close()

# [NEW] Task: Read using readline()
# The worksheet asks to read lines individually using readline() calls.
print("8. Reading line-by-line manually:")
file_var = open("info.txt", "r")
print(file_var.readline(), end='') # Line 1
print(file_var.readline(), end='') # Line 2
print(file_var.readline(), end='') # Line 3
file_var.close()
print("\n")

# Task: Loop reading
print("9. Reading with a loop:")
file_var = open("info.txt", "r")
for line in file_var:
    print(line, end='')
file_var.close()
print("\n")

# Task: Appending
print("10. Appending a new line...")
file_var = open("info.txt", "a")
file_var.write("this is an extra line\n")
file_var.close()

# Task: The 'with' statement
print("11. Reading with the 'with' statement:")
with open("info.txt", "r") as f:
    for line in f:
        print(line, end='') 

print("\n\n--- ALL TASKS COMPLETED ---")