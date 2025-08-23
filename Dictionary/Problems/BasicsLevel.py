# Basic Level
# 1. Create and Access Dictionary
# Problem:
# Create a dictionary student with keys name, age, and grade. Print the value of grade.

student = {"name": "Kaushal", "age": 18, "grade": "A"}
print(student["grade"])

# 2. Add and Update Dictionary Elements
# Problem:
# Create a dictionary car with keys brand and model. Add a new key year and update the model value.

car = {"brand": "BYD", "model": "2022"}
car["year"] = "2023"
print(car)
car["model"] = "2023"
print(car)

# 3. Check if Key Exists
# Problem:
# Write a program to check if the key "salary" exists in the dictionary employee = {"name": "John", "age": 30}.
employee = {"name": "John", "age": 30}
value = employee.get("salary", "no")
if value == "no":
    print("salary is not exist")
else:
    print("salary is exist")

# OR

if "salary" in employee:
    print("salary exists")
else:
    print("salary does not exist")

# 4. Loop Through Dictionary
# Problem:
# Given fruits = {"apple": 100, "banana": 40, "mango": 80}, print all keys and values in the format:
# apple -> 100

fruits = {"apple": 100, "banana": 40, "mango": 80}
for key, value in fruits.items():
    print(key, "->", value)

# 5. Delete Dictionary Element
# Problem:
# Remove the key age from person = {"name": "Alice", "age": 25, "city": "London"} and print the updated dictionary.
person = {"name": "Alice", "age": 25, "city": "London"}
person.pop("age")
print(person)

# 6. Length of Dictionary
# Problem:
# Find how many keys exist in my_dict = {"a": 10, "b": 20, "c": 30}.
my_dict = {"a": 10, "b": 20, "c": 30}
print(len(my_dict))
