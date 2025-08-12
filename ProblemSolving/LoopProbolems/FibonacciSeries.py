# Write a Program to get Fibonacci series up to 10 numbers.
n = 10
a = 0
b = 1
for i in range(1, n - 1):
    if i == 1:
        print(a)
        print(b)
    c = a + b
    a = b
    b = c
    print(c)


