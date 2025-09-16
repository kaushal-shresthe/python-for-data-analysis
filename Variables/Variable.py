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

# Example 1: Small integers (cached in memory)
a = 50   # Python creates an integer object 50 and 'a' points to it
b = 50   # Python reuses the same cached object 50, so 'b' points to the same memory as 'a'
print(id(a))  # id() shows the memory address (object identity) of 'a'
print(id(b))  # Same as 'a', because both refer to the same object (50 is cached)

# Example 2: Larger integers (not always cached)
x = 1000  # Python creates a new integer object 1000
y = 1000  # Python usually creates another new integer object 1000
print(id(x), id(y))   # Usually different ids, because 1000 is outside the cached range (-5 to 256)




