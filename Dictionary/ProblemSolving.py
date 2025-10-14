# User function Template for python3
# n = int(input())
#
# # Your code here
# for i in range(0, n):
#     print("*", end=" ")
# print()
# space = " "
# for i in range(0, n - 2):
#     print("*", end=" ")
#     print(" " * (n), end="")
#     print("*")
#
# for i in range(0, n):
#     print("*", end=" ")
# print()
#

for i in range(1, 5):
    for j in range(1, 5 - i):
        print(" ", end=" ")
    for k in range(0, 2*i - 1):
        print(k + 1, end=" ")
    print()

