# Q1. Check if a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2. Find the largest among three numbers.
a, b, c = input("Enter three number: ").split(" ")
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print(f"{a} is largest among three numbers.")
elif b > c:
    print(f"{b} is largest among three numbers.")
else:
    print(f"{c} is largest among three numbers.")

# Q3. Write a program to check if a year is a leap year.
year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
