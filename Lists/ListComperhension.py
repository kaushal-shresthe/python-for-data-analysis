# Without Using List Comprehension
list1 = [4, 6, 7, 5, 4, 3, 3]
list2 = []
for i in list1:
    if i > 4:
        list2.append(i)
print(list1, "\n", list2)

# With List Comprehension
list3 = [i for i in list1]
print(list3)

# List Comprehension With Condition
list4 = [i for i in list1 if i < 5]
print(list4)

# Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# Create a list of even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

# Convert a list of strings to uppercase
words = ["apple", "banana", "cherry"]
upper_words = [x.upper() for x in words]
print(upper_words)
