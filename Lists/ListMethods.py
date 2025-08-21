ages = [23, 32, 43, 21, 23, 45, 32, 23]
print(ages)

# to find the length of a list
print(len(ages))

# to count an accurence of a particular element
print(ages.count(23))

# to add to the list
ages.append(30)
print(ages)

# to add to a specific location
ages.insert(2, 41)
print(ages)

# to remove from a list
ages.remove(23)
print(ages)

# to remove from a certain location
print(ages.pop(2))
print(ages)

# to create a copy of a list
duplicate = []
print(duplicate)
duplicate = ages.copy()
print(duplicate)

# to access an element
print(ages.index(23))
print(ages.index(23, 2, 6))
print(ages.index(23, 5))

# to extend the list
ages1 = [10, 12, 13]
ages.extend(ages1)
print(ages)

# to reverse the list
ages.reverse()
print(ages)

# to sort the list
ages.sort()
print(ages)

# to clear all the data from the list
ages.clear()
print(ages)