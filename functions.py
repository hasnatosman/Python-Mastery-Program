# Functions
# Functions help organize and reuse code.
# Defining functions using def
# Calling functions
# Function parameters
# Return values
# Default parameters
# Keyword arguments
# Variable length arguments
# Lambda functions
# Anonymous functions
# Using lambda with simple operations

# Practice:
# Calculator using functions
# Temperature conversion functions

# Defining and calling functions
def great_user():             # def: defines a function & great_user: function name
    print('Hello, welcome!')

great_user()                  # calling function

# function parameter
def great_user(user_name):          # user_name is a parameter
    print(f'Hello, {user_name}')

great_user('John Smith!')           # Value 'John Smith' is passed as an argument


# Return values

def add_numbers(number1, number2):
    return number1 + number2

result = add_numbers(20,10)
print(result)

# Default Parameter

def great_user(user_name = 'Guest'):     # here, user_name has a default parameter
    return f"Hello, {user_name}"

user1 = great_user()
user2 = great_user('Alex')               # now, it passed an argument, will not count as default
print(user1)
print(user2)

# Note: Default parameter must come last

# Positional argument
def describe_pet(animal, name):
    return f"I have a {animal} named {name}."

pet1 = describe_pet('Dog', 'Ben')
pet2 = describe_pet('Cat', 'Tom')

print(pet1)
print(pet2)

# Keyword Parameter

def student_info(name, age):
    return f"Name: {name}, Age: {age}"

student1 = student_info(name='Rafi', age = 25)
student2 = student_info(age = 30, name = 'Rehan')

print(student1)
print(student2)

# Variable length argument

# *args: multiple positional arguments
# you need to accept an unknown number of items
# the * packs all extra positional arguments into a tuple

def add_all_numbers(*number):
    return sum(number)

total1 = add_all_numbers(1,2,3)
total2 = add_all_numbers(4,5,6,7)
print(total1)
print(total2)

# **kwargs: multiple keyword argument
# you need to accept an unknown number of named items
# the ** packs all extra keyword arguments into a dictionary

def build_profile(**user_info):
    return user_info
user1 = build_profile(name='rafkat', age = 25, country = 'UK')
print(user1)


def print_user_info(**user_data):
    for key, value in user_data.items():
        print(key, ':', value)

print_user_info(name = 'hasnat', age = 30, country = 'uk')

# Lambda functions (anonymous functions)
# oneline function
# no def keyword
# used for simple operation only

add = lambda number_one, number_two: number_one + number_two
print(add(100,200))

# lambda with map
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda number: number ** 2, numbers))

print(squared_numbers)

# map() applies function to each item

# Practice
# Calculator using function

def add(number_one, number_two):
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide(number_one, number_two):
    if number_two == 0:
        return " Can not divide by zero"
    return number_one / number_two

print(add(10,5))
print(divide(10,5))
print(multiply(10,5))
print(divide(10,5))


# Temperature Conversion
def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit_value):
    return (fahrenheit_value - 32) * 5 / 9

print(celsius_to_fahrenheit(25))
print(fahrenheit_to_celsius(77))