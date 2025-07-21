'''
- A set is a collection of unordered(No indexing or slicing allowed), unindexed, and
 unique(Duplicate values are automatically removed)elements.
- Defined using curly braces {} or the set() constructor.
- Sets automatically remove duplicates.
'''

# Creating a Set
numbers = {1, 2, 7, 4, 5, 6}
print(numbers)

# Adding Elements
numbers.add(5)
print("After Add:", numbers)

# Removing Elements

# Removing Elements
numbers.remove(3)     # Removes 3 – throws error if not found
print("After removing 3:", numbers)  # {1, 2, 4, 5}

numbers.discard(10)   # Removes 10 – no error if not found
print("After discarding 10 (not present):", numbers)  # {1, 2, 4, 5}

removed_item = numbers.pop()         # Removes a random element
print("Removed item using pop():", removed_item)
print("After popping an item:", numbers)

numbers.clear()       # Removes all elements
print("After clearing the set:", numbers)  # set()

# Set operations

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5} - Combines sets
print(a.intersection(b)) # {3} - Common items
print(a.difference(b))   # {1, 2} - Items in set1 but not in set2
print(b.difference(a))   # {4, 5}
print(a.symmetric_difference(b)) # {1, 2, 4, 5} - Items not common in both sets
