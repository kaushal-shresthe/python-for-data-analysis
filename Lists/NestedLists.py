# Lists can contain other lists to represent matrices or tables.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # 2 → first row, second column


# iterating the nested list
for i in range(0, 3):
    for j in range(0, 3):
        print(matrix[i][j], end=" ")
    print()

