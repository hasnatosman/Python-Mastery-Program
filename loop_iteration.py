# Loops and Iteration
# This module explains repetitive tasks using loops.
# while loop
# for loop
# Using range()
# Nested loops
# Loop control statements: break,continue, pass
# Practice:
# Multiplication table generator
# Number guessing game
# Pattern printing

# While condition: runs while condition is True

# count = 1
# while count <= 5:
#     print(f"Count: {count}")
#     count += 1

# starts from count = 1
# runs untile count <= 5
# count +=1: increase value, without value increase, infinite loop

# for loop: used when number of iterations is known

for number in range(1,6):
    print(number)

# range(1,6) : 1 to 5

# range: start,stop,step
print(list(range(5)))
print(list(range(1,10)))
print(list(range(1,10,2)))


# Nested loops

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# Loop controls
# break: stop loop completely

for number in range(1,10):
    if number == 5:
        break
    print(number)


# continue: skip current iteration

for number in range(1,10):
    if number == 5:
        continue
    print(number)

# pass: do nothing

for number in range(1,10):
    pass


# Practice
# Multiplication Table Generator

number = int(input("Enter a number: "))

for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")

# Number Guessing Game

secret_number = 7
attempt_limit = 3

for attempt in range(attempt_limit):
    guess = int(input("Enter a number: "))

    if guess == secret_number:
        print('You guessed right!')
        break
else:
    print('Game Over!')