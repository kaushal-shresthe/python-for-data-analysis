# What is a String?
# -> A string in Python is a sequence of characters enclosed in single quotes ('),
# double quotes ("), or triple quotes (''' or """).
# -> Strings are used to store text.

# 1. Creating Strings
# -> Strings can be enclosed in:
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple quotes
for multi-line strings'''

# -> Triple quotes preserve formatting and line breaks.

# 2. Indexing & Slicing
# -> Strings are ordered sequences, so we can use:

word = "Python"

# Indexing
print(word[0])   # P
print(word[-1])  # n

# Slicing
print(word[0:3])  # Pyt
print(word[2:])   # thon
print(word[:4])   # Pyth
print(word[::-1]) # nohtyP (reverse string)

# 3. String Concatenation & Repetition
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World
print(a * 3)        # HelloHelloHello

# 4. String Methods (Built-in Functions)

# Case Conversion
txt = "python is fun"
print(txt.upper())    # PYTHON IS FUN
print(txt.lower())    # python is fun
print(txt.title())    # Python Is Fun
print(txt.capitalize()) # Python is fun
print(txt.swapcase()) # PYTHON IS FUN -> python is fun

# Whitespace Handling
msg = "   hello world   "
print(msg.strip())   # removes spaces both sides
print(msg.lstrip())  # removes left spaces
print(msg.rstrip())  # removes right spaces

# Searching
txt = "I love Python"
print(txt.find("love"))   # 2 (index)
print(txt.rfind("o"))     # 10 (last 'o')
print(txt.index("Python")) # 7 (error if not found)
print(txt.count("o"))     # 2
print(txt.count("o", 6, 13))

# Replacing

txt = "I like Java"
print(txt.replace("Java", "Python")) # I like Python

# Splitting & Joining
text = "apple,banana,orange"
print(text.split(","))  # ['apple', 'banana', 'orange']
words = ["Python", "is", "fun"]
print(" ".join(words))  # Python is fun

# Checking Content
name = "Kaushal"
print(name.isalpha())   # True (only letters)
print(name.isdigit())   # False (not only numbers)
print("123".isdigit())  # True
print("hello123".isalnum())  # True (letters + numbers)
print("hello".islower())  # True
print("HELLO".isupper())  # True
print(" ".isspace())    # True (only whitespace)

# It fills the given character and centralizes a string
name = "Kaushal Shrestha"
print(name.center(20, "*"))


# String Formatting
# f-strings (best way)
name = "Kaushal"
age = 18
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# old % formatting
print("My name is %s and I am %d years old." % (name, age))

# 5. Escape Characters
#-> Escape sequences allow special characters inside strings:
print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab space
print("He said \"Python is fun\"") # Quotes inside string

# 6. Raw Strings
# -> Raw strings ignore escape sequences:
print(r"C:\newfolder\test")  # C:\newfolder\test

# 7. Useful Advanced Tricks
txt = "Python"
print(txt[::-1])  # Reverse string
print("".join(sorted(txt))) # 'Phnoty' (sorted alphabetically)
print("*".join("ABC")) # A*B*C

# 8. String Immutability
# -> Strings cannot be changed in place:

s = "Python"
# s[0] = "J"  # ERROR
s = "J" + s[1:]
print(s)  # Jython


# Some String Method
a = "Kaushal Shrestha"
# endswith() - Returns true if the string ends with the specified value
print(a.endswith("a"))
print(a.endswith("h", 3, 8))

# startswith() - Returns true if the string starts with the specified value
print(a.startswith("K"))
print(a.startswith("k"))
print(a.startswith("h", 4, 10))

# swapcase() - Swaps case lower case to upper case and vice versa
print(a.swapcase())

# strip() - Returns a trimmed version og the string
a = "     ***** Kaushal ............."
print(a)
print(a.strip("*, "))

# split() = Splits the string at the specified separator, and returns a list
a = "00FD#BRM#OEM#KID"
b = "hello. my nmae is kaushal shrestha. i am 23 years old"
c = "Ram Sita Gita Rita Hari Buddhi"
print(a.split("#"))
print(b.split("."))
print(c.split(" "))

# ljust() - Returns a left justified version of the string
a = "Pokhara"
x = a.ljust(20, "_")
print(x, "is my favorite place")

# rjust() -  Returns a right justified version of the string
x = a.rjust(20, "_")
print(x, "is my favorite place")

# rindex() - Searches the string for a specified value and returns the last position of where it was found
a = "My name is Kaushal Shrestha"
print(a.rindex("Kaushal"))
print(a.rindex("h", 8, 15))
