cars = ["Audi", "Fortuner", "BMW", "Tesla"]

# Iteration Using for loop
for car in cars:
    print(car)

# Iteration Using for loop with range and length function
for car in range(len(cars)):
    print(cars[car])

# Iteration using while loop
i = 0
while i < len(cars):
    print(cars[i])
    i = i + 1

# Using Short-hand for loop
[print(i) for i in cars]

