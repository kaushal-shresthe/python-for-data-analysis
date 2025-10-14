# Dictionary allows user to write the data in the form of keys and values.
# -> Dictionaries are enclosed inside curly brackets {}.
# -> Keys and values are separated by colon
# -> Every key value pair is separated by a comma(,).
# -> Key Must be Unique

Employee_Data = {"Name": "Jhon", "Age": 24, "Gender": "Male"}
print(Employee_Data)
print(Employee_Data["Name"])

# Creating Dictionaries
# Using curly braces
d = {"a": 1, "b": 2}
print(d)
# Using dict() constructor
d = dict(x=10, y=20)
print(d)  # {'x': 10, 'y': 20}

# Empty dictionary
empty_dict = {}
print(type(empty_dict))

# Accessing Elements
# Using keys
student = {"name": "Kaushal", "age": 18}
print(student["name"])  # Kaushal

# Using get() method
print(student.get("age"))     # 18
print(student.get("course"))  # None (does not exist)
print(student.get("course", "Not Found"))  # Not Found

# Iteration in Dictionary
# Printing all the key names one by one
for E in Employee_Data:
    print(E)

# OR

for E in Employee_Data.keys():
    print(E)

# Printing all the value one by one
for E in Employee_Data:
    print(Employee_Data[E])

# OR

for E in Employee_Data.values():
    print(E)

# Printing all key and values
for E in Employee_Data.items():
    print(E)

# OR

for K, V in Employee_Data.items():
    print(f"Key :{K}, value: {V} ")

print(Employee_Data[0])

# Adding & Updating Elements
student = {"name": "Kaushal", "age": 18}

# Adding new key-value pair
student["course"] = "BCA"
print(student)

# # Updating existing key
student["age"] = 19
print(student)
