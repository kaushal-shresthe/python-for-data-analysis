a = [1, 2, 3]
b = a          # b refers to the same list object as a
c = [1, 2, 3]  # c is a different list object with the same content

print("a is b:", a is b)         # True (same object)
print("a is c:", a is c)         # False (different objects, same content)

print("a is not c:", a is not c) # True (not the same object)

# Use '==' to compare values, 'is' to compare identity
print("a == c:", a == c)         # True (values are equal)
