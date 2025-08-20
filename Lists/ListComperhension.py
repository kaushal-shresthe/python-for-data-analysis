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

