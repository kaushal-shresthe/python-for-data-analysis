a = 10
b = 5
c = 20

# and: both conditions must be True
print("a > b and c > a:", a > b and c > a)  # True and True → True

# or: at least one condition must be True
print("a > b or b > c:", a > b or b > c)    # True or False → True

# not: reverses the result
print("not(a > b):", not(a > b))            # not(True) → False

age = 22
citizen = True

# Check if eligible to vote
if age >= 18 and citizen == True:
    print("You can vote.")
else:
    print("You cannot vote.")
