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

# Write a program check whether the passed letter is a vowel or not
# Method 1
letter = input("Enter a letter: ").lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(f"{letter} is a vowel letter")
else:
    print(f"{letter} is not a vowel letter")


# Method 2
letter = input("Enter a letter: ").lower()
if len(letter) == 1 and letter.isalpha():
    if letter in "aeiou":
        print(f"{letter} is a vowel letter.")
    else:
        print(f"{letter} is not a vowel letter.")
else:
    print("Please enter a single alphabet character.")


# Program to check if a number is single-digit, 2-digit, ..., up to 5-digit
num = input("Enter number: ").replace(" ", "")

if num.startswith("-"):
    num = num[1:]

if not num.isdigit():
    print("Invalid input. Please enter a valid number.")
else:
    length = len(num)

    if length == 1:
        print("Single-digit number")
    elif length == 2:
        print("2-digit number")
    elif length == 3:
        print("3-digit number")
    elif length == 4:
        print("4-digit number")
    elif length == 5:
        print("5-digit number")
    else:
        print("More than 5-digit number")


