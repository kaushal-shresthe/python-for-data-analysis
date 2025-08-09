# Multiplication table using while loop
n = 1
num = int(input("Enter the number here: "))

while n <= 10:
    print(f"{num} * {n} = {num * n}")
    n = n + 1

# Write a program to find sum of first 10 odd numbers using while loop
count = 1
i = 1
result = 0
while count <= 10:
    if i % 2 != 0:
        result += i
        count = count + 1
    i = i + 1
print(f"Sum of first 10 odd numbers is {result}")


