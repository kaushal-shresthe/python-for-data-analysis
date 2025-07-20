a = 10  # This line creates a variable 'a' and assigns it the integer value 10.
        # In Python, integers are immutable and small integers (like -5 to 256) are cached (interned).

b = 10  # This line creates another variable 'b' and also assigns it the value 10.
        # Since 10 is a small integer, Python doesn't create a new object — it reuses the same one from memory.

print(a, b)  # This will print the values of 'a' and 'b', which are both 10.
             # Output: 10 10

print(id(a), id(b))  # The id() function returns the "identity" of an object — basically, its memory address.
                     # Since both 'a' and 'b' are pointing to the same integer object 10,
                     # their id() values will be the same.
                     # Output: (something like) 140732709586672 140732709586672 (IDs will be same)


x = 1100
y = 1000

print(x, y)
print(id(x), id(y))

c = "hello"
print(a)

# 1a = 20 wrong

a_b = 34
print(a_b)

_a = 10
print(_a)
