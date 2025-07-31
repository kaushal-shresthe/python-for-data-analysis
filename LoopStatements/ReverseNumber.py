# Reverse a number using a while loop

num = 56423
rnum = 0

while num > 0:
    rem = num % 10
    rnum = rem + rnum * 10
    num = num // 10

print(f"The Reverse number is {rnum}")
