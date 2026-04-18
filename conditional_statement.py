# Conditional Statements
# This module introduces decision making in programs.
# if statement
# if-else statement
# if-elif-else structure
# Nested conditions
# Logical condition combinations
# Practice:
# Grade evaluation program
# Even / odd checker
# Login verification system


# Conditional statement
# Used for decision-making, program runs different code based on conditions

# if statement

age = 20
if age >= 20:
    print('you are an adult!')

# condition: age >= 18
# if True: print message
# if False: nothing happens


# if else statement

number = int(input("Enter a number: "))

if number > 0:
    print('Positive number.')
else:
    print('Negative number.')

# only one block runs
# either if or else

# if - elif - else statement

marks = int(input("Enter marks: "))
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print('B')
else:
    print('Fail')
#
# # Nested conditions
age = int(input("Enter age: "))
has_id_card = True

if age >= 18:
    if has_id_card:
        print('Allowed')
    else:
        print('ID required')

else:
    print('Not allowed')

# Logical condition combination

age = int(input('Enter your age: '))
citizen = True

if age > 18 and citizen:
    print('Eligible to vote!')

# Practice
# Grade evaluation program

marks = int(input("Enter your marks: "))

if marks >= 80:
    grade = 'A+'
elif marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'Fail'

print(f"Your grade is: {grade}")

# Even odd checker

number = int(input("Enter your number: "))

if number % 2 == 0:
    print(f"{number} is Even Number!")
else:
    print(f"{number} is odd number!")

# Login Verification System


correct_username = 'admin'
correct_password = '12345'

username = input('Enter username: ')

if username == correct_username:
    password = input('Enter password: ')

    if password == correct_password:
        print('Login successful!')
    else:
        print('Wrong password!')
else:
    print('Username not found!')