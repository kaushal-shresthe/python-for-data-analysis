# Variables and Data Types
x = 25
y = 7.5
name = "Kaushal"
is_student = True

print("x =", x, "| type:", type(x))
print("y =", y, "| type:", type(y))
print("name =", name, "| type:", type(name))
print("is_student =", is_student, "| type:", type(is_student))

# Useful Functions with Variables
# type() → Returns the data type of a variable.
x = 100
print(type(x))

# id() → Returns the unique memory address (identity) of a variable.
a = 50
b = 50
print(id(a))
print(id(b))  # may be same (Python reuses small integers)

# isinstance(object, class) → Checks if a variable is an instance of a specific data type.
x = 3.14
print(isinstance(x, float))  # True
print(isinstance(x, int))    # False
