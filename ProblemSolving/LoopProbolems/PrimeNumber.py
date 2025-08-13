# Check Number is Prime or not [
num = int(input("Enter a Number: "))
temp = num // 2
count = 0
if num == 2:
    print("Prime")
elif num < 1:
    print("Enter Greater than 1")
else:
    for i in range(2, temp + 1):
        if num % i == 0:
            count = count + 1
            break

    if count == 0:
        print("Prime")
    else:
        print("Not Prime")
