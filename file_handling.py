# File Handling
# This module explains how Python interacts with files.
# Opening files
# File modes:read,write,append
# Reading files
# Writing files
# Working with text files
# Best practices using with statement
# Practice:
# Log file analyzer
# Data storage program

# Opening files
file = open('example.txt', 'r')    # 'example.txt' file name 'r' mode(read)
file.close()

# Reading file
file = open('example.txt', 'r')

content = file.read()
print(content)

file.close()

# Writing files
file = open('example.txt', 'w')
file.write('i really love you.')
file.write('so much.')

file.close()

# Reading file
file = open('example.txt', 'r')

content = file.read()
print(content)

file.close()

# Appending files
file = open('example.txt', 'a')
file.write('\nNew line added.')
file.close()


# Best practices
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# auto close
# cleaner code
# safer