# Working with string
text = "hello"

print("'e' in text:", 'e' in text)        # True
print("'z' in text:", 'z' in text)        # False
print("'H' not in text:", 'H' not in text)  # True

# Working with list
numbers = [1, 2, 3, 4, 5]

print("3 in numbers:", 3 in numbers)      # True
print("10 in numbers:", 10 in numbers)    # False
print("6 not in numbers:", 6 not in numbers)  # True

# Working with dictionary (checks for keys only)
student = {'name': 'John', 'age': 20}

print("'name' in student:", 'name' in student)      # True
print("'John' in student:", 'John' in student)      # False (value, not key)
print("'grade' not in student:", 'grade' not in student)  # True
