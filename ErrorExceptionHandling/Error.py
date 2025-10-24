# Type of Errors in Python
# When writing Python programs, error can occur, which are broadly classified into syntax errors and exceptions

# Syntax Errors
# -> Errors that occur when the code violates Python's syntax rules
# -> Detected before the program runs(at compile-time)

# Examples
# Missing Colon
# if True
#     print("Hello")

# Invalid assignment
# 5 = x

# Runtime Errors (Exceptions)
# -> Definition: Errors that occur during program execution.
# -> These are called exceptions.
# -> Program may stop running unless exceptions are handled.

# ZeroDivisionError
num = 5 / 0

# IndexError
lst = [1, 2, 3]
print(lst[5])

# Logical Errors
# -> Definition: Program runs but produces incorrect output due to wrong logic.
# -> Not detected by Python; programmer must debug.

# Logical error
a = 10
b = 5
avg = a + b / 2  # Incorrect formula
print(avg)       # Output: 12.5 (correct should be 7.5)


