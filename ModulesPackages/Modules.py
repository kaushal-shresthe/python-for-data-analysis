# Importing and using a module
# Example
import math

print(math.sqrt(4))

# Importing specific functions
from math import pi, pow

print(pi)
print(pow(2, 3))

# Using alias
import math as m

print(m.factorial(5))

# Using Multiple Built-in Modules
import math
import random
import datetime

print(math.ceil(4.2))
print(random.randint(1, 10))
print(datetime.datetime.now())

