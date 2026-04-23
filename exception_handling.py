# Exception Handling
# This module teaches how to manage runtime errors.
# Understanding errors and exceptions
# try / except block
# Handling multiple exceptions
# else clause
# finally clause
# Raising exceptions
# Practice:
# Safe division program
# Input validation system


# Understanding Errors vs Exceptions
# Error: Problem in code(syntax error)
# Exception: Happens during runtime(program run but crashes)

# Syntax Error( won't run)
# print("Hello

# Exception ( runs but crashes)
# number = int('abc') # value error

# try / except block: used to prevent program crash

try:
    number = int(input('Enter a number: '))
    print(f"You entered: {number}")

except:
    print('Invalid input')

# try: risky code
# except: runs if error happens

# Handling Specific Exceptions

try:
    number = int(input('Enter a number: '))
    result = 10 / number
    print(result)
except ValueError:
    print('Please enter a valid number.')

except ZeroDivisionError:
    print('Cannot divide by zero')

# Multiple Exception in one line
try:
     number = int(input('Enter a number: '))
     result = 10 / number
     print(result)

except(ValueError, ZeroDivisionError):
     print('Invalid input or division error')

# Else clause
try:
    number = int(input('Enter number: '))
except ValueError:
    print('Invalid input')
else:
    print('Success! You entered: ',number)


# Finally Clause: always runs(error or no error)
try:
    file = open('data.txt')
    content = file.read()

except FileNotFoundError:
    print('File not found.')
finally:
    print('Execution finished.')


# Raising Exceptions (Custom errors)

age = int(input('Enter your age: '))

if age < 18:
    raise ValueError('Age must be 10 or above.')
print('Access Granted.')

# Practice 1: Safe Division Program
def safe_division():
    try:
        numerator = float(input('Enter numerator: '))
        denominator = float(input('Enter denominator: '))

        result = numerator / denominator

    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    except ValueError:
        print('Invalid input')
    else:
        print('Result: ', result)
    finally:
        print('Operation Completed!')

safe_division()

# Input validation system

def get_valid_age():
    while True:
        try:
            age = int(input('Enter your age: '))

            if age <= 0:
                raise ValueError('Age must be positive.')
            return age
        except ValueError as error:
            print('Error: ', error)

age = get_valid_age()
print('Valid age: ', age)