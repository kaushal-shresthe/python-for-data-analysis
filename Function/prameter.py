# 1. Positional Parameters
# These are the most common. Arguments are passed in the same order as parameters.
def add(a, b):
    return a + b


print(add(5, 3))


# 2. Default Parameters
# we can give a parameter a default value, which is used if no argument is passed.
def greet(name="Guest"):
    print("Hello,", name)


greet()
greet("Alice")


# 3. Keyword Arguments
# we can pass arguments using name=value, so order doesn’t matter.

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce(age=25, name="Bob")


# 4. Arbitrary Positional Arguments (*args)
# If we don’t know how many arguments will be passed, use *args.
# It collects arguments into a tuple.
def add_all(*numbers):
    return sum(numbers)


print(add_all(2, 4, 6))  # Output: 12
print(add_all(1, 2, 3, 4))  # Output: 10


# 5. Arbitrary Keyword Arguments (**kwargs)
# If we don’t know how many named arguments will be passed, use **kwargs.
# It collects arguments into a dictionary.
def show_info(**person):
    for key, value in person.items():
        print(f"{key}: {value}")


show_info(name="Alice", age=22, country="USA")


# Docstring
# The first string after the function is called the Document string or Docstring in short.
# This is used to describe the functionality of the function. The use of docstring in functions is optional
# but it is considered a good practice.

# Syntax: print(function_name.__doc__)

def evenOdd(x):
    """Function to check if the number is even or odd"""

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


print(evenOdd.__doc__)

