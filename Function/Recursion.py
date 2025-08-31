# What is Recursion?
# Recursion is when a function calls itself to solve a problem.
# Every recursive function must have:
#
# Base Case -> condition to stop recursion (otherwise infinite loop).
# Recursive Case -> the function calls itself with smaller/simpler input.

# Example 1: Factorial (Classic Recursion)
# The factorial of n is:
# n!=n×(n−1)×(n−2)×...×1

def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n-1)  # recursive case


print(factorial(5))

# How it works:
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120


# Example 2: Fibonacci Sequence
# Fibonacci:
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    if n == 0:   # base case 1
        return 0
    elif n == 1: # base case 2
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive case


print(fibonacci(6))

# Example 3: Recursion with a List
# Sum of a list:


def list_sum(lst):
    if not lst:   # base case: empty list
        return 0
    return lst[0] + list_sum(lst[1:])  # recursive case


print(list_sum([1, 2, 3, 4]))

# Important Notes
# Recursion must have a base case -> otherwise Python throws RecursionError.
# Python has a recursion limit (default ~1000 calls). we can check it:

import sys
print(sys.getrecursionlimit())

# Recursion is elegant, but sometimes loops are more efficient.
