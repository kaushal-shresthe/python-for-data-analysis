# math Module -> Provides mathematical functions.
import calendar
import math

print(math.sqrt(16))       # 4.0  → square root
print(math.factorial(5))   # 120  → factorial
print(math.ceil(4.3))      # 5    → round up
print(math.floor(4.7))     # 4    → round down
print(math.pi)             # 3.141592653589793

# random Module -> Used for generating random numbers and selections.
import random

print(random.randint(1, 10))   # Random integer between 1-10
print(random.choice([1, 2, 3]))      # Randomly select from a list
print(random.shuffle([1, 2, 3, 4]))     # Shuffle list in place

# datetime Module -> Provides date and time manipulation.
import datetime

now = datetime.datetime.now()
print(now)                # Current date and time
print(now.year)           # Current year
print(now.strftime("%d-%m-%Y"))  # Formatted date
print(now.strftime("%Y/%m/%d"))

# os Module -> Used for operating system interactions.:
import os

print(os.getcwd())       # Current working directory
print(os.listdir())      # List files in current directory
# os.mkdir("test_folder")  # Create a folder

# sys Module -> Provides access to Python runtime environment.:
import sys

print(sys.version)       # Python version
print(sys.path)          # Search path for modules

# collections Module -> Provides specialized data structures.
from collections import Counter, defaultdict

lst = [1, 2, 2, 3, 3, 3]
print(Counter(lst))      # Count occurrences: {1:1, 2:2, 3:3}

d = defaultdict(int)
d["a"] += 1
print(d)                 # defaultdict(<class 'int'>, {'a': 1})

# itertools Module -> Provides efficient looping and combinations.
import itertools

print(list(itertools.permutations([1, 2, 3], 2)))  # All 2-element permutations
print(list(itertools.combinations([1, 2, 3], 2)))  # All 2-element combinations

# functools Module -> Provides higher-order functions, decorators, and functional programming tools.
from functools import reduce

nums = [1, 2, 3, 4]
sum_total = reduce(lambda x,y: x+y, nums)
print(sum_total)  # 10

# re Module -> Provides regular expressions for pattern matching.
import re

text = "My number is 12345"
pattern = r"\d+"  # Match one or more digits
result = re.findall(pattern, text)
print(result)  # ['12345']
