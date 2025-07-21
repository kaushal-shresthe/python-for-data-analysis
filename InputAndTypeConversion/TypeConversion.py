'''
Type conversion means changing the data type of a value from one type to another.

👉 Python provides two types of conversion:

1. Implicit Conversion	Automatically done by Python
2. Explicit Conversion	Done manually using functions (int(), str(), etc.)
'''


#  Implicit Type Conversion
# Python automatically converts one data type to another without losing data.

a = 5       # int
b = 2.5     # float

c = a + b   # int + float → float
print(c)    # 7.5
print(type(c))  # <class 'float'>

# Explicit Type Conversion
# Also called type casting –  manually convert data types.

# int to float
a = 10
b = float(a)
print(b)         # 10.0
print(type(b))   # <class 'float'>

# float to int
x = 5.7
y = int(x)
print(y)         # 5 (decimal part removed)

# int to string
num = 100
text = str(num)
print(text)      # "100"
print(type(text))  # <class 'str'>

# string to int
s = "50"
n = int(s)
print(n + 10)    # 60

# list to set
l = [1, 2, 3, 3]
s = set(l)
print(s)         # {1, 2, 3}

# list to tuple
t = tuple(l)
print(t)         # (1, 2, 3, 3)

# ⚠️ Notes:
# We cannot convert a string like "abc" to int – it will raise an error.
# We can convert "123" to int using int("123").

''''
When you get user input using input(), it’s always a string.
If you’re unsure whether the input is int, float, list, etc., 
you can use eval() to auto-convert the string to its correct Python data type.'''


x = input("Enter any value: ")  # Always string
print(type(x))                  # <class 'str'>

x = eval(x)                     # Converts based on input
print(type(x))                  # Type depends on what you entered

'''
⚠️ Warning:
eval() can execute any valid Python expression, so never use it on untrusted input. 
It can be dangerous, especially in web applications.
'''