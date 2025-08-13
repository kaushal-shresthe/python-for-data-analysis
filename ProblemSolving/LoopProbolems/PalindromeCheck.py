# Write a Program to check a palindrome number.
num = int(input("Enter a number to Check Palindrome: "))
temp = num
print(temp)
rem = 0
Reverse = 0
while num > 0:
    rem = num % 10
    Reverse = Reverse * 10 + rem
    num = num // 10

if temp == Reverse:
    print(f"{temp} is a Palindrome number.")
else:
    print(f"{temp} is not a Palindrome number.")