# Lambda functions are anonymous (unnamed) functions in Python.
# They are used for short, single-line functions.
# Syntax is compact and ideal for simple operations.

# Example 1: Simple lambda
square = lambda x: x**2
print(square(5))

# Example 2: Lambda with multiple arguments
add = lambda a, b: a + b
print(add(10, 15))

# Example 3: Using lambda inside map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Example 4: Using lambda inside filter()
numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Example 5: Using lambda inside sorted()
students = [("Kaushal", 18), ("Sita", 20), ("Mohan", 17)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


