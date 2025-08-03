# Write a Program to display a person's name, age and address in three different lines.

name = "Kaushal Shrestha"
age = 23
address = "Pokhara"

# Method 1
print(name)
print(age)
print(address)

# Method 2
print(f"{name}\n{age}\n{address}")

# Write program to swap two variable

# Method 1
x = 12
y = 10
print(f"Before Swapping: x = {x} and y = {y}")

temp = x
x = y
y = temp
print(f"After Swapping: x = {x} and y = {y}")

# Method 2
a = 20
b = 10
print(f"Before Swapping: a = {a} and Y = {b}")

# left, right = right, left
a, b = b, a
print(f"After Swapping: a = {a} and Y = {b}")


# Write a program to convert a float into integer

k = 2.34
print(f"Before type casting: k = {k}, {type(k)}")
k = int(k)
print(f"After type casting: k = {k}, {type(k)}")

# Write a program to take details from a student for ID-card then print it in different lines.

print("Enter the Student Details")
name = input("Enter the Name of the Student: ")
grade = input("Enter the Grade of the Student: ")
age = int(input("Enter the Age of the Student: "))
email = input("Enter the Email of the Student: ")
ph_no = input("Enter the Phone of the Student: ")

print("Student Identity Card")
print(name)
print(grade)
print(email)
print(ph_no)

# Write a program to take on user input as integer then convert it to float

num = int(input("Enter the an integer number: "))
print(f"Your entered number is {num} and type is {type(num)}")

num = float(num)
print(f"After Converting your entered number into float, i.e {num} and type is {type(num)}")


