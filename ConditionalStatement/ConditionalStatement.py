# if Statement

age = 18

if age >= 18:
    print("You are eligible to vote.")

#  if...else Statement
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You are not eligible to vote.")

#  if...elif...else Statement
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Fail")

# Nested if Statement
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("You can vote.")
    else:
        print("You are not a citizen.")
else:
    print("You are underage.")


# Short Hand if and if...else (Ternary Operator)
# Short Hand if
a = 10
b = 5
if a > b: print("a is greater")

# Short Hand if...else
# Example 1
print("a" if a > b else "b")

# Example 2
marks = 80
print("you will go to trip") if marks >= 80 else print("no phone for one month")


# ❌ Is There a switch Statement in Python?
# No, Python does not have a built-in switch or case statement like C, Java, or JavaScript.
# ✅ But You Can Use if...elif...else or a Dictionary Instead.

# Using if...elif...else
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid day")

# Using Dictionary as a switch-like structure
def switch_case(day):
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday"
    }.get(day, "Invalid day")

print(switch_case(3))   # Output: Wednesday
print(switch_case(7))   # Output: Invalid day

#  Using match-case (Python 3.10+ only)
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

# ✅ match-case is Python’s modern alternative to switch from version 3.10+.