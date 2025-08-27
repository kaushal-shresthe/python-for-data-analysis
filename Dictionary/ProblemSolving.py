# User function Template for python3
n = int(input())

# Your code here
for i in range(0, n):
    print("*", end=" ")
print()
space = " "
for i in range(0, n - 2):
    print("*", end=" ")
    print(" " * (n), end="")
    print("*")

for i in range(0, n):
    print("*", end=" ")
print()
