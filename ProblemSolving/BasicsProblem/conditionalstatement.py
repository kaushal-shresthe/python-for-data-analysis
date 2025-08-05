# Write a program to check if a number is positive
num = int(input("Enter a number: "))
if num > 0:
    print("It is positive")

# Write a program to check whether a number is even or odd
number = int(input("Enter another number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Write a program to create a calculator
operator = input("Enter operator ('+','-','*','/'): ")  # FIXED: Typo in closing quote
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Math error: division by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator. Please use one of: '+', '-', '*', '/'")
