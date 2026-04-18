# Input Function and Operators
# This module introduces interaction with users and Python operators.
# User input
# Using the input() function
# Converting input values
# Operators
# Arithmetic operators: Addition,Subtraction, Multiplication, Division, Modulus, Exponent
# Comparison operators: Equal,Not equal,Greater than,Less than
# Logical operators: and, or, not
# Assignment operators: =,+=,-=,*=,/=
from pythoPractice import height

# Practice:
# Age calculator
# Simple BMI calculator


# User Input: take data from user(keyboard) & always return string(str)

# student_name = input("Enter student name: ")
# print(f"Hello, This is {student_name}.")

# even if user types a number, it is still string, then need type casting

# Arithmatic operators

num1 = 10
num2 = 3

print(num1 + num2)         # addition
print(num1 - num2)         # subtraction
print(num1 * num2)         # multiplication
print(num1 / num2)         # Division
print(num1 // num2)        # Floor Division
print(num1 % num2)         # Modulus(remainder)
print(num1 ** num2)        # Exponent


# comparison operators

num1 = 10
num2 = 3

print(num1 == num2)       # Equal
print(num1 != num2)       # Not Equal
print(num1 > num2)        # Greater than
print(num1 < num2)        # Less Than
print(num1 >= num2)       # Greater or equal
print(num1 <= num2)       # Less or equal

# Logical operators

age = 20

print(age > 18 and age < 30)     # Both must be True
print(age > 18 or age < 30)      # At least one True
print(not(age < 30))             # Reverse Result

# Assignment Operators
x = 10                    # assign
print(x)
x += 2                    # x = x + 2
print(x)
x -= 5                    # x = x - 5
print(x)
x *= 2                    # x = x * 2
print(x)
x /= 3                    # x = x / 3
print(x)


# Practice

# Age Calculator
# current_year = int(input("Enter current year: "))
# birth_year = int(input("Enter your birth year: "))
#
# age = current_year - birth_year
#
# print(f"Your age is: {age}")

# Simple BMI calculator

# take input from user
weight_kg = float(input("Enter your weight(KG): "))
height_m = float(input("Enter your height(meter): "))

# calculate BMI
bmi_score = weight_kg / (height_m ** 2)

print(f"Your BMI is: {round(bmi_score)}")