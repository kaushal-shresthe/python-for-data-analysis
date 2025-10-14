# 1. Nested Dictionary Access
# Print salary of emp2 from:
data = {
    "emp1": {"name": "John", "salary": 5000},
    "emp2": {"name": "Alice", "salary": 7000}
}
print(f"Salary of the emp2: {data['emp2']['salary']}")

# Update Value in Nested Dictionary
# Update emp1 salary to 6000 in the above dictionary.
data["emp1"]["salary"] = 60000
print(data["emp1"])

# Dictionary Comprehension (Squares)
# Create {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} using dictionary comprehension.

Squares1 = {i: (i ** 2) for i in range(1, 6)}
print(Squares1)

# OR

Squares = {}
for i in range(1, 6):
    Squares[i] = i ** 2
print(Squares)

# Reverse Dictionary (Keys ↔ Values)
# Convert d = {"a": 1, "b": 2, "c": 3} to {1: "a", 2: "b", 3: "c"}.
d = {"a": 1, "b": 2, "c": 3}
c = {}
for key, value in d.items():
    c[value] = key
print(c)

# Group by Length of Word
# Given words = ["apple", "bat", "cat", "banana"], group them by word length:
# {3: ["bat", "cat"], 5: ["apple"], 6: ["banana"]}.
words = ["apple", "bat", "cat", "banana"]
length = {}
for word in words:
    l = len(word)
    if l not in length:
        length[l] = []
    length[l].append(word)
print(length)

# Find Common Keys in Two Dictionaries
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 20, "c": 30, "d": 40}
# Output: ['b', 'c'].

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}
output = []
for key1 in dict1:
    for key2 in dict2:
        if key1 == key2:
            output.append(key1)
print(output)

# OR

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

common_keys = list(dict1.keys() & dict2.keys())
print(common_keys)

# Nested Dictionary from Two Lists
# Convert:
# students = ["John", "Alice"]
# scores = [85, 90]
# to:
# {"student1": {"name": "John", "score": 85}, "student2": {"name": "Alice", "score": 90}}.

students = ["John", "Alice"]
scores = [85, 90]
nesteddict = {}

for i in range(len(students)):
    nesteddict[f"student{i+1}"] = {"name": students[i], "score": scores[i]}

print(nesteddict)

# Count occurrences of characters in a string
text = "python programming"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)

# Filter dictionary based on values
scores = {"Alice": 85, "Bob": 72, "Charlie": 90}
high_scores = {k: v for k, v in scores.items() if v > 80}
print(high_scores)

# Student Grades (Nested Dictionary + List)
students = {
    "Kaushal": [85, 90, 88],
    "Maya": [78, 82, 80]
}
for student, marks in students.items():
    print(f"{student}: Average = {sum(marks)/len(marks)}")
