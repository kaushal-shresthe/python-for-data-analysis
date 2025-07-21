# Convert Input to int
a = input("Enter your age: ")
print(type(a))  # <class 'str'>
# Note: Input from user is always taken as a string by default

age = int(input("Enter your age again: "))
print("Next year you will be", age + 1)

# Convert Input to float
height = float(input("Enter your height in meters: "))
print("Your height is", height)

# Convert to Boolean
value = bool(input("Type something: "))  # Empty string is False, non-empty is True
print("Boolean value is:", value)
