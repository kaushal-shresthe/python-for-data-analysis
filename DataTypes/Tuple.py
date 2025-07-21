# Creating Tuples

t1 = (1, 2, 3)                  # With multiple values
t2 = (5,)                       # Single value tuple (note comma)
t3 = ()                         # Empty tuple
t4 = ("apple", 1, True, 2.5)    # Mixed data types

'''📝 Note (Very Important):
In a tuple, the values must be comma-separated.
If you don’t add a comma in a single-element tuple, Python will not treat it as a tuple.'''

# ❌ Incorrect (Not a tuple):
t = (5)
print(type(t))  # Output: <class 'int'>

# ✅ Correct (Single-element tuple):
t = (5,)
print(type(t))  # Output: <class 'tuple'>

# Accessing Tuble Elements
print(t1[0])        # 1
print(t1[-1])       # 3
print(t1[1:3])      # (2, 3)

# Tuple Methods
t = (1, 2, 3, 2, 4)
print(t.count(2))   # 2
print(t.index(3))   # 2


# Why Use Tuples?
# - Faster than lists (performance)
# - Data protection (immutability)
# - Used as keys in dictionaries (only immutable types allowed)

