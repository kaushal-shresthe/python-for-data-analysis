# Lists can contain other lists to represent matrices or tables.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # 2 → first row, second column

# Accessing Elements
print(matrix[0])      # [1, 2, 3]  -> first row
print(matrix[1][2])   # 6          -> 2nd row, 3rd column

# Modifying Nested Lists
matrix[2][1] = 80
print(matrix)

# iterating the nested list
for i in range(0, 3):
    for j in range(0, 3):
        print(matrix[i][j], end=" ")
    print()

# Transpose a 2x3 matrix using nested lists.
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transpose)
