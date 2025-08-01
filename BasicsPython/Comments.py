# Single-line comments
# Start with # and continue to the end of the line.


# This is a single-line comment
print("Hello, World!")  # This comment is after code

# Multi-line comments (docstrings or block comments)
# Python doesn’t have a specific syntax for multi-line comments, but you can use:
# Triple quotes (''' or """) (typically used for docstrings, but can act as multi-line comments).
# Multiple single-line comments (#).

'''
This is a multi-line comment
using triple quotes (often used for docstrings).
'''

"""
Another way to write
multi-line comments.
"""

# Alternatively, you can use multiple
# single-line comments for
# multi-line explanations.

# Best Practices:
# Use comments to explain why something is done, not what is done (the code itself should be clear).
# Avoid excessive comments; write self-documenting code when possible.
# Example with a docstring (used for function documentation):

def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b