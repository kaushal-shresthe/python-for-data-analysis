# Dictionary Methods

# 1 .keys() ->  returns all keys
Employee_Data = {"Name": "Jhon", "Age": 24, "Gender": "Male"}
print(Employee_Data.keys())


# 2. .values() -> returns all values
print(Employee_Data.values())

# 3 .items() -> returns all key–value pairs as tuples
print(Employee_Data.items())

# 4 .get(key, default) -> safely get value by key (no error if key missing)
print(Employee_Data.get("Age"))
print(Employee_Data.get("Salary", 0))


# 5 .update({...}) -> update dictionary with new key-value pairs
Employee_Data.update({"Age": 18})
Employee_Data.update({"Salary": 50000})
print(Employee_Data)


# 6 .pop(key)-> removes and returns the value of the given key
x = Employee_Data.pop("Age")
print(x)
print(Employee_Data)

# 7 .popitem() -> removes and returns the last inserted key-value pair
print(Employee_Data.popitem())
print(Employee_Data)

# 8 .clear() -> removes all items from dictionary
Employee_Data.clear()
print(Employee_Data)


# 9 .copy() -> returns a shallow copy of dictionary
copy_dict = Employee_Data.copy()
print(copy_dict)

# 10 .fromkeys(keys, value) -> create new dictionary from keys with same value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# 11 .setdefault(key, default) -> returns value of key; if key not exists, insert with default value
# Example of .setdefault(key, default)
Employee_Data = {"Name": "Jhon"}

# "Age" key does not exist → adds "Age": 25 and returns 25
print(Employee_Data.setdefault("Age", 25))   # Output: 25

# "Age" key already exists → keeps "Age": 25, returns existing value (25), ignores 23
print(Employee_Data.setdefault("Age", 23))   # Output: 25

# Final dictionary: {"Name": "Jhon", "Age": 25}
print(Employee_Data)

