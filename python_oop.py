# Object Oriented Programming (OOP)
# This module introduces object-oriented programming concepts.
# Classes and objects
# Creating classes
# Attributes and methods
# Constructors (__init__)
# Instance variables
# Class variables
# Instance methods
# Practice:
# Student management class
# Bank account system

# What is OOP?
# Object-Oriented programming is a way to structure code using objects.
# Class: blueprint
# object: real instance of class

# Basic class & object
class Student:
    pass # empty

# create object
student_one = Student()
print(student_one)

# class Student: defines a class
# student_one = Student(): creates an object
# each object is a unique instance

# attributes & methods

class Student:
    def __init__(self, name, age):
        self.name = name            # attribute
        self.age = age              # attribute

    def display_info(self):         # method
        print(f'Name: {self.name}, Age: {self.age}')

student_one = Student('Hasnat', 25)
student_one.display_info()


# __init__: constructor(run automatically)
# self: current object reference
# self.name: instance variable
# display_info: instance method

# Instance vs class variable
class Student:
    school_name = 'ABC school'        # class variable

    def __init__(self, name):
        self.name = name              # instance variable

student_one = Student('Hasnat')
student_two = Student('Rahim')

print(student_one.school_name)
print(student_two.school_name)


# Instance Methods

class Calculator:

    def add(self, number_one, number_two):
        return number_one + number_two

calculator = Calculator()
result = calculator.add(10,5)
print(result)


# Practice
# Student management system

class Student:
    school_name = 'ABP School'

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_student(self):
        print(f'School:{self.school_name}')
        print(f'Name:{self.name}')
        print(f'Marks:{self.marks}')


    def is_passed(self):
        return self.marks >= 40

student_one = Student('Hasnat', 50)
student_two = Student('Rahim', 30)

student_one.display_student()
print('Passed:', student_one.is_passed())
print()

student_two.display_student()
print('Passed:', student_two.is_passed())



# Bank account System

class BankAccount:
    bank_name = 'ABC Bank'

    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposite: {amount}")
        else:
            print('Invalid Amount!')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Balance!')
        elif amount <= 0:
            print('Invalid withdrawal amount!')
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f'Account holder name: {self.account_holder}')
        print(f'Balance: {self.balance}')


account = BankAccount('Rahim', 10000)

account.deposit(1000)
account.withdraw(500)
account.check_balance()