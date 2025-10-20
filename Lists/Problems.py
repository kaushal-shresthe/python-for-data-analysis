A = ["Ross", "Rachel", "Monica", "Joe"]

# Write a Program to swap first and fourth element
print(f"Before Swap: {A}")
A[0], A[3] = A[3], A[0]
print(f"After Swap: {A}")

# Write a Program to add a new value at second position
A.insert(1, "Phoebe")
print(A)

# Write a program to delete a value from 3rd position
print(A.pop(2))
print(A)

B = [13, 7, 12, 10]

# Write a program to mutliply all the element in the list
mul = 1
for i in B:
    mul = mul * i
print(mul)

# Write a program to get the largest and smallest number from the list
B.sort()
print(f"Largest value is {B[-1]}")
print(f"Smallest value is {B[0]}")

# Concatenate [1,2,3] and [4,5] and multiply the result by 2.
list1 = [1, 2, 3]
list2 = [4, 5]
result = (list1 + list2) * 2
print(result)
