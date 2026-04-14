# This module focuses on converting data and formatting output.
# Type casting
# int()
# float()
# str()
# bool()
# Implicit vs explicit conversion
# Formatted string literals (f-strings)
# Formatting numbers and text
# Practice:
# Creating formatted output reports
# Converting user input into numbers

# Type casting means converting one data type into another.

integer_value = int("10")        # string → int
float_value = float("10.5")     # string → float
string_value = str(100)         # int → string
boolean_value = bool(1)         # int → bool

# print(type(integer_value))
# print(type(float_value))
# print(type(string_value))
# print(type(boolean_value))

print(int(10.9))     # 10 (decimal removed)
print(int("50"))     # 50

print(float(10))     # 10.0
print(float("3.14")) # 3.14

print(str(100))      # "100"

print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool("text"))  # True

# Implicit vs Explicit Conversion

# Python converts automatically:

result = 10 + 5.5

print(result)        # 15.5
print(type(result))  # float

# Explicit (Manual)
# You convert yourself:

number = "20"

converted_number = int(number)

print(converted_number + 5)   # 25

# Formatted String Literals (f-strings)

# Basic Example
name = "Hasnat"
age = 25

print(f"My name is {name} and I am {age} years old.")

# Expression inside f-string
a = 5
b = 6

print(f"Sum is { a + b}")

# Formatting Numbers & Text

# Decimal formatting

price = 99.5677

print(f"Price: {price:.2f}")

# Alignment

name = "Python"

print(f"{name:<10}")   # left aligned
print(f"{name:>10}")   # right aligned
print(f"{name:^10}")   # center aligned

# Thousands separator

salary = 1000000

print(f"Salary: {salary:,}")   # 1,000,000

# practice
# Formatted output report


student_name = "Rahim"
marks = 87.333
passed = False

report = f"""
Student Report
-----------------
Name  : {student_name}
Marks : {marks:.2f}
status: {"Passed" if passed else "Failed"}
"""
print(report)

# Simple Calculator

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

sum = first_number + second_number

print(f"Total = {sum:.2f}")