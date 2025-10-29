# Factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(6))

# Fibonacci series up to n
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2
for i in range(7):
    print(fibonacci(i), end=" ")

# Sum of digits of a number
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))

# Check if a string is palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))
print(is_palindrome("python"))

# Decimal to Binary using recursion
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n//2) + str(n%2)

print(decimal_to_binary(10))

# Count occurrences of an element in a list
def count_occurrences(lst, x):
    if not lst:
        return 0
    return (lst[0] == x) + count_occurrences(lst[1:], x)

print(count_occurrences([1,2,3,2,2,4], 2))

# Find power of a number (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

# Sum of first n natural numbers
def sum_n(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + sum_n(n-1)  # Recursive case

print("Sum of first 5 natural numbers:", sum_n(5))

# Reverse a string using recursion
def reverse_string(s):
    if s == "":
        return s  # Base case
    else:
        return reverse_string(s[1:]) + s[0]  # Recursive step

print(reverse_string("Kaushal"))

# Greatest Common Divisor (GCD) using recursion
def gcd(a, b):
    if b == 0:  # Base case
        return a
    else:
        return gcd(b, a % b)  # Recursive step

print("GCD of 48 and 18:", gcd(48, 18))


# Tower of Hanoi Problem
# Problem: Move n disks from source peg to target peg using auxiliary peg, one disk at a time,
# larger disk cannot be on smaller disk.
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

tower_of_hanoi(3, 'A', 'C', 'B')
