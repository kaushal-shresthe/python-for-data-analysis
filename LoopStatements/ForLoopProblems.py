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


# Write a program to write first 20 numbers and their squared numbers
print("Number    Square")
for i in range(1, 21):
    print(f"{i}          {i**2}")

# Write a program to check if a number is divisible by 8 and  12, up to 100 numbers
print("Number is divisible by 8 and  12, up to 100 numbers:")
for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)





