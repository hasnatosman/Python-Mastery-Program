# Python Data Structures
# This module focuses on storing and managing collections of data.
# Lists
# Creating lists
# Accessing elements
# Indexing
# Slicing
# List methods:
# append()
# insert()
# remove()
# pop()
# sort()
# reverse()
# Practice:
# Student marks list
# Finding maximum and minimum values

# Tuples
# Creating tuples
# Tuple packing and unpacking
# Tuple indexing
# Tuple immutability
# Practice:
# Coordinate data storage

# Sets
# Creating sets
# Unique values in sets
# Set operations:
# union
# intersection
# difference
# symmetric difference

# Practice:
# Removing duplicates from data

# Dictionaries
# Key-value pairs
# Creating dictionaries
# Accessing dictionary values
# Adding and updating keys
# Dictionary methods
# keys()
# values()
# items()
# get()
# Practice:
# Student information database
# Word frequency counter


# What is a list?
# An ordered, mutable collection. Items have index positions and can be changed after creation.

# Creating list
student_marks = [86, 90, 92, 88]
print(student_marks)

# list stores multiple values, ordered and mutable(can change)

# Accessing elements(indexing)
print(student_marks[0])        # first element: 86
print(student_marks[1])        # second element or 1st index: 90
print(student_marks[-1])

# index starts from 0
# negative index = from end

# Slicing
print(student_marks[0:2])       # start:end -> end is excluded
print(student_marks[:])

# List methods

numbers = [2,3,7,11,45,89,56,88,77]
print(numbers)

numbers.append(99)                     # add at the end
numbers.insert(1,5)     # insert at 1st index
numbers.remove(56)                     # remove value
numbers.pop()                          # remove last item
numbers.sort()                         # sort ascending
numbers.reverse()                      # reverse list

print(numbers)

# practice
marks = [75, 88, 92, 60, 79]

maximum_marks = max(marks)
minimum_marks = min(marks)

print('Max:', maximum_marks)
print('Min:', minimum_marks)

# Tuple: ordered, immutable
# Creating tuple

location = (40.7128, -74.0060) # creating & packing

lat, long = location      # unpacking
print(f'Latitude: {lat}, Longitude: {long}')

# practice
location = (23.5, 90.4)
print(f'Latitude: {location[0]}')
print(f'Longitude: {location[1]}')


# Set : unordered, mutable, no duplicates

numbers = {1,5,2,3,7,5,9}
print(numbers)     # automatically removes duplicate

# set operation
set_a = {1,2,3}
set_b = {3,4,5}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))

# Practice: remove duplicate

data = [1,2,5,6,3,8,9,4,6,9]

unique_data = list(set(data))
print(unique_data)


# Dictionary: stores data in key_value pairs, mutable, uniques keys

# creating a student info dictionary
student = {
    'name': 'Asif Khan',
    'age': 25,
    'dept': 'cse',
    'cgpa': 2.94,
    'course': ['python', 'dsa', 'dbms']

}

# accessing values  by key
print(student['name'])
print(student['age'])
print(student['course'])

# get() - safe access, returns None if key not found
print(student.get('age'))
print(student.get('country'))
print(student.get('dept'))

# adding 8 updating keys
student['phone'] = 22993311       # creating key
student['cgpa'] = 3.94            # updating key

print(student)


# dictionary methods
print(list(student.keys()))             # keys() : all key as a view
print(list(student.values()))           # Values() : all values as a view
print(list(student.items()))            # items(): all key-value pairs as tuple


# iterating with items
for key, value in student.items():
    print(f'{key}: {value}')


# Practice: student information database

# database of multiple students using nested dicts
database = {
    'S001': {'name': 'Hasnat', 'cgpa': 2.94, 'dept': 'cse'},
    'S002': {'name': 'Hasan', 'cgpa': 3.44, 'dept': 'eee'},
    'S003': {'name': 'Hafiz', 'cgpa': 2.64, 'dept': 'tex'},
    'S004': {'name': 'Hannan', 'cgpa': 3.34, 'dept': 'bba'}
}

print(database)

# access a specific student
print(database['S002']['dept'])
print(database['S001']['dept'])


# practice: word frequency counter

text = ' the cat sat on the mat and watching outside, but the cat is not playing'
words = text.split()

# count each word's frequency using a dictionary
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)



























