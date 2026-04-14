# Module 2 ---------------------------------------

#  Variables and Data Types
# This module explains how Python stores and manages data.
# Understanding variables
# Variable naming rules and best practices
# Python keywords
# Built-in data types:
# Integer
# Float
# String
# Boolean
# Checking data types using type()
# Dynamic typing in Python
# Practice:
# Creating variables
# Performing calculations using variables


# What is variable?
# Variable is like a container where we can store date

student_name =  "Hasnat"         # here, student_name is variable name & "Hasnat" is value,
student_age = 25                 # here, student_age is variable & 25 is value

# Rules:
# letter diye start korte hobe
# number thakte pare (but start e na)
# underscore _ use korte paro
# space use kora jabe na

# Best practice
# always use meaningful name

x = 10                    # doesn't mean anything
student_id = 10           # means he is a student with id number 10

# python keywords
# Python e kichu reserved words ase
# Egula variable name hisebe use kora jabe na
# Example: if, else, for, while, True, False, None, def, class


# Built-in Data Types

# Integer (int) → Whole number
product_number = 10

# Float → Decimal number
product_price = 99.99

# String → Text
product_name = "Pizza"

# Boolean → True / False
is_large = True

# Check Data Type (type())

print(type(product_number))
print(type(product_price))
print(type(product_name))
print(type(is_large))

# Dynamic Typing
# Python e type manually dite hoy na
# Automatically change hoy

x = 50
print(type(x))
x = 'any text'
print(type(x))

# practice
# Creating variables
value1 = 100
value2 = 200

# performing calculations using variable
value1 = 100
value2 = 200

sum_of_two = value1 + value2

print("Total of two values: ",sum_of_two)
