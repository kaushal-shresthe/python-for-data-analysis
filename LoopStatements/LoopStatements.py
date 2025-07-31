
# What is a Loop?
"""
A loop is used to repeat a block of code multiple times until a certain condition is met.
Loops help reduce redundancy and automate repetitive tasks.
"""

# Types of Loops in Python:
"""
-> for loop – used to iterate over a sequence (like list, string, tuple).
-> while loop – runs as long as a given condition is True.
-> nested loops – a loop inside another loop.
"""

# 1. for Loop
"""
The for loop is used to iterate over a sequence like a list, tuple, dictionary, string, or range.

Synt
ax:
for variable in sequence:
    # code block
    
"""
# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() with for loop:
for i in range(1, 6):
    print(i)


# 2. while Loop
"""
The while loop repeats as long as the condition is True.
Syntax:
while condition:
      # code block
"""

# Example:
count = 1
while count <= 5:
    print(count)
    count += 1


# 3. Nested Loops
"""
A loop inside another loop is called a nested loop.
Useful for working with matrices, patterns, combinations, etc.
"""

# Example:
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# break and continue in Loops

# break – Exits the loop early
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# continue – Skips the current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

