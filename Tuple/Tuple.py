# Tuples are the collection of ordered and un-mutable data.
# -> for tuples no brackets are mandatory. By choice one can use parentheses.
# -> The value inside a Tuple is separated by comma(,).
# -> Once created, tuples cannot be changed.
# -> Multiple datatypes can be written inside a tuples.

a1 = "apple", "bannna", "mango"
print(type(a1))

a2 = ("apple", "bannna", "mango")
print(type(a2))

a3 = "apple"
print(type(a3))

a4 = "apple",
print(type(a4))

a5 = ("apple")
print(type(a5))

a6 = ("apple",)
print(type(a6))

# Slicing and Iteration in Tuples
Mobiles = ("OnePlus", "Vivo", "Redmi", "SumSung", "Nokia", "Apple")
print(Mobiles[1:3])
print(Mobiles[2:])
print(Mobiles[::2])
print(Mobiles[1::2])
print(Mobiles[::-1])
print(Mobiles[-1])
print(Mobiles[2::-1])

# Along With range length in for loop
for i in range(len(Mobiles)):
    print(Mobiles[i])

# Along with while loop
i = 0
while i < len(Mobiles):
    print(Mobiles[i])
    i += 1

# List Functions
print(Mobiles.count("Nokia"))

print(f"The index of Redmi {Mobiles.index("Redmi")}")

# Conversion of Tuple
print(f"Before Conversion {type(Mobiles)}")
Mobiles = list(Mobiles)
print(f"After Conversion {type(Mobiles)}")

Mobiles.append("Poco")
Mobiles = tuple(Mobiles)
print(Mobiles)
