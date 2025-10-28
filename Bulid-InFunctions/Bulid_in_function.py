# len() -> Returns the length (number of items) of an object (string, list, tuple, dictionary, etc.).
# String
print(len("Python"))

# List
print(len([1, 2, 3, 4]))

# Dictionary (number of keys
print(len({"a": 1, "b": 2}))

# max() and min()
# -> max() returns the largest item.
# -> min() returns the smallest item.
numbers = [10, 5, 30, 20]

print(max(numbers))
print(min(numbers))

# String example
print(max("Python")) #(ASCII order)
print(min("Python"))

# sum() -> Returns the sum of all elements in an iterable (list, tuple, set).
nums = [10, 20, 30]
total = sum(nums)
print(total)

# sorted()
# -> Returns a sorted list from an iterable.
# -> Default is ascending order, use reverse=True for descending.
numbers = [3, 1, 5, 2]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# String example
print(sorted("Python"))
print(sorted("Python", reverse=True))

# abs() -> Returns the absolute value of a number.
print(abs(-10))
print(abs(5))

# round() -> Rounds a floating-point number to the nearest integer or specified decimal places.
print(round(3.6))       # 4
print(round(3.14159, 2))  # 3.14

# int(), float(), str()
# -> Convert values from one type to another.
# -> Useful for type casting when performing arithmetic or string operations.
# int conversion
print(int("10"))

# float conversion
print(float("3.5"))

# string conversion
print(str(100))

# type() -> Returns the data type of a variable or object.
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Python"))  # <class 'str'>

# id() -> Returns the unique identity (memory address) of an object.
a = 10
b = 10
print(id(a))
print(id(b))  # Same as a because integers are immutable and shared

# range() -> Generates a sequence of numbers.
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5

#all() and any()
print(all([True, True, False]))  # False
print(any([True, True, False]))  # True

# enumerate()
names = ["Kaushal", "Hari"]
for idx, name in enumerate(names):
    print(idx, name)

# zip()
a = [1, 2, 3]
b = ["A", "B", "C"]
print(list(zip(a,b)))  # [(1,'A'),(2,'B'),(3,'C')]

# reversed()
print(list(reversed([1, 2, 3])))  # [3,2,1]
