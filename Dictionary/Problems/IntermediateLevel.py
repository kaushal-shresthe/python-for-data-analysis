# Intermediate Level

# 1. Count Frequency of Elements in a List
# numbers = [1, 2, 2, 3, 1, 4, 2] → Output: {1: 2, 2: 3, 3: 1, 4: 1}.

numbers = [1, 2, 2, 3, 1, 4, 2]
count = {}
for i in numbers:
    value = numbers.count(i)
    count[i] = value
print(count)

# 2. Merge Two Dictionaries
# Merge:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
for key, value in dict2.items():
    dict1[value] = key
print(dict1)

# 3. Sort Dictionary by Keys
# Sort scores = {"Ram": 85, "Shyam": 92, "Hari": 78} by keys in ascending order.
scores = {"Ram": 85, "Shyam": 92, "Hari": 78}
keys = []
for key in scores.keys():
    keys.append(key)
keys.sort()
print(keys)

# 4. Sort Dictionary by Values (Descending)
# Sort scores = {"Ram": 85, "Shyam": 92, "Hari": 78} by values in descending order.
scores = {"Ram": 85, "Shyam": 92, "Hari": 78}
values = []
for value in scores.values():
    values.append(value)
values.sort()
print(values[::-1])

# 5. Find Key with Maximum Value
# In marks = {"A": 90, "B": 85, "C": 92}, find the student with the highest marks.
marks = {"A": 90, "B": 85, "C": 92}
highest = 0
name = ""
for key, value in marks.items():
    if value > highest:
        highest = value
        name = key
print(f"Stundent {name} score the highest marks i.e {highest}")

# 6. Dictionary from Two Lists
# Convert:
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "London"]
# to {"name": "Alice", "age": 25, "city": "London"}.

keys = ["name", "age", "city"]
values = ["Alice", 25, "London"]
new_dict = {}
for i in range(0, 3):
    for j in range(0+i, i+1):
        new_dict[keys[i]] = values[j]

print(new_dict)

# Remove Duplicates from Dictionary Values
# Given d = {"a": 1, "b": 2, "c": 1, "d": 3}, remove duplicate values and keep unique key-value pairs
