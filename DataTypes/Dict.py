# A dictionary is an unordered, mutable, and indexed collection of key-value pairs.
# Each item has a unique key and an associated value.
# Defined using curly braces {}.


# Creating dict
student = {
    "Name": "Kaushal",
    "Age": 18,
    "Course": "BCA"
}

print(student)


#  Accessing Dictionary Elements
print(student["Name"])
print(student["Age"])

# Modifying Dictionary
student["Age"] = 19
student["Course"] = "B.Tech"

# Removing Elements
student.pop("Age")  # Remove key "Age"
# student.clear()  # Clears the entire dictionary

# Dictionary Methods

student = {
    "Name": "Kaushal",
    "Age": 18,
    "Course": "BCA"
}

print(student.keys())     # Returns all keys: dict_keys(['Name', 'Age', 'Course'])
print(student.values())   # Returns all values: dict_values(['Kaushal', 18, 'BCA'])
print(student.items())    # Returns all key-value pairs as tuples

# Update dictionary with another dictionary
student.update({"Age": 19, "College": "LA Grandee"})
print(student)  # Updated dictionary

# Remove item with specified key
student.pop("Name")
print(student)  # 'Name' key removed

# Remove all items from the dictionary
student.clear()
print(student)  # Output: {}
