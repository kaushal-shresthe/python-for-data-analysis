# Function ->A function is a block of code that performs a specific task.
# It helps you reuse code instead of writing it multiple times.

# Defining a Function
# In Python, you define a function using the def keyword:

def greet():
    print("Hello, welcome to Python!")

# Here:
# def → tells Python you are defining a function
# greet → function name
# () → parentheses (can hold inputs/parameters)
# : → starts the function body
# Indented code → function body

# Calling a Function
# To run(call) afunction, just use its name with parentheses:
greet()

# Functions with Parameters
def greet_user(name):
    print("Hello,", name)
greet_user("Alice")
greet_user("Bob")

# Functions with Return Values
# Functions can also return values:
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

