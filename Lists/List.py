# Python Lists - Basics and Examples
# A List is a collection of ordered and mutable data.
# -> Ordered means elements have a fixed position/index.
# -> Mutable means elements can be changed after creation.
# -> Lists are written inside square brackets [].
# -> Items inside a list are separated by commas (,).
# -> Lists can store multiple data types.

# Example 1: Simple list of strings
fruits = ["apple", "mango", "banana"]
print(fruits)
print(type(fruits))

# Example 2: List with multiple data types
details = ["Kaushal Shrestha", 18, "Pokhara"]
print(details)
print(type(details))


# Accessing and Slicing Lists

# List of countries
country = ["Nepal", "USA", "China", "Russia", "Australia"]

# Accessing elements using index
print(country[1])               # USA (Index starts from 0)

# Slicing examples
print(country[1:3])              # ['USA', 'China'] -> from index 1 to 2
print(country[0:2])              # ['Nepal', 'USA'] -> from index 0 to 1
print(country[1:])               # ['USA', 'China', 'Russia', 'Australia'] ->  from index 1 to end
print(country[::2])              # ['Nepal', 'China', 'Australia'] -> gap of 2
print(country[::-1])             # ['Australia', 'Russia', 'China', 'USA', 'Nepal'] ->  reversed list

# Looping through a List
for fruit in fruits:
    print(fruit)

# Using index in loop
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Checking if an item exists
if "apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")
