# Write a program to find the largest among three numbers using nested if-else statements.
print("Enter three number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is largest number")
    else:
        print(f"{num3} is largest number")
else:
    print(f"{num2} is largest number")
