Employee_Data = {
    "E001": {"Name": "Sam", "Age": 24, "Gender": "Male"},
    "E002": {"Name": "Alice", "Age": 28, "Gender": "Female"},
    "E003": {"Name": "Bob", "Age": 30, "Gender": "Male"}
}

print(Employee_Data)

# Iterate nested dictionary
for employee, info in Employee_Data.items():
    print(employee)
    for k, v in info.items():
        print(f"  {k}: {v}")

# Accessing Data
print(Employee_Data["E003"]["Age"])
print(Employee_Data["E002"]["Gender"])

# Updating Data
Employee_Data["E001"]["Age"] = 25
Employee_Data["E002"]["Salary"] = 50000

print(Employee_Data)

# Looping Through Nested Dictionaries
for emp_id, details in Employee_Data.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")

# Adding a New Employee
Employee_Data["E004"] = {"Name": "David", "Age": 26, "Gender": "Male", "Salary": 45000}
print(Employee_Data)

# Taking Input from User
emp_id = input("Enter Employee ID: ")
name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
Employee_Data[emp_id] = {"Name": name, "Age": age, "Gender": gender}

print("\nUpdated Employee Data:")
for emp_id, details in Employee_Data.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")

# Adding Multiple Employees Dynamically
for i in range(2):
    emp_id = input("\nEnter Employee ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    Employee_Data[emp_id] = {"Name": name, "Age": age, "Gender": gender}
print("\nFinal Employee Data:", Employee_Data)