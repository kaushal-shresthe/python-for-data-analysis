# Using split() with strings
name, city = input("Enter name and city: ").split()
print("Name:", name)
print("City:", city)


# With Type Conversion using map()
a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)
