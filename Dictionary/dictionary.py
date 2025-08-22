# Dictionary allows user to write the data in the form of keys and values.
# -> Dictionaries are enclosed inside curly brackets {}.
# -> Keys and values are separated by colon
# -> Every key value pair is separated by a comma(,).
# -> Key Must be Unique

Employee_Data = {"Name": "Jhon", "Age": 24, "Gender": "Male"}
print(Employee_Data)
print(Employee_Data["Name"])

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
