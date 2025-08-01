
# Input and Type Conversion in Python

# Convert Input to String (Default behavior)
a = input("Enter your age: ")  # Takes input as a string by default
print(type(a))                 # Output: <class 'str'>

# Convert Input to Integer
age = int(input("Enter your age again: "))  # Converts input string to integer
print("Next year you will be", age + 1)

# Convert Input to Float
height = float(input("Enter your height in meters: "))  # Converts input string to float
print("Your height is", height)

# Convert Input to Boolean
value = bool(input("Type something: "))
# An empty string ('') returns False, and a non-empty string returns True
print("Boolean value is:", value)


# 🔍 Using eval() to Automatically Detect and Convert Input

# What is eval()?
# eval() is a built-in Python function that takes a string as input
#  and evaluates it as a valid Python expression.

# Syntax:
# eval(expression)

# 🔸 Example:
user_input = eval(input("Enter any valid Python expression: "))
print("Evaluated result:", user_input)
print("Data type:", type(user_input))

# 💡 Sample Inputs and What They Return:
# Input: 5 + 3           → Output: 8                 → Type: int
# Input:print("Kaushal") → Output: Kaushal           → Type: NoneType
# Input: [1, 2, 3]       → Output: [1, 2, 3]         → Type: list
# Input: (4 + 6) * 2     → Output: 20                → Type: int
# Input: {'a': 1}        → Output: {'a': 1}          → Type: dict
# Input: True            → Output: True              → Type: bool


# ⚠️ Warning: eval() is Powerful but Dangerous
# eval() can execute **any code**, not just simple expressions.
# If someone enters a malicious command, it could harm your system.

# For example:
# Input: __import__('os').system('rm -rf /')
# This is dangerous and could delete files (in real usage).

# 👉 So NEVER use eval() on input from untrusted users in real-world applications!


# ✅ Safer Alternative: ast.literal_eval
# If you only want to safely evaluate basic data types like
# numbers, strings, lists, dicts, tuples — use `literal_eval`.

# from ast import literal_eval
# safe_input = literal_eval(input("Enter number, list, or string: "))
# print("Result:", safe_input)
# print("Type:", type(safe_input))

# literal_eval prevents code execution and only parses literal values.
