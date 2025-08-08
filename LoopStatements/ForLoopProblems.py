# Print all even numbers between 1 - 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Multiplication table
num = int(input("Enter the number for which you need the multiplication table: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")


# Sum of First 10 Natural Numbers:
result = 0
for i in range(1, 11):
    result = result + i
print(f"Sum of First 10 Natural Numbers: {result}")


# Reverse a String: Take a string input from the user and print its reverse using a for loop.
UserInput = input("Enter String input: ")
length = len(UserInput)
reversed_string = ""
for i in range(1, length+1):
    reversed_string += UserInput[-i]
print(f"Reversed String: {reversed_string}")

