# Pattern 1: Right-Angled Triangle
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

# Pattern 2: Number Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Pattern 3: Reverse Triangle
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1, 6):
    for j in range(6 - i):
        print("*", end=" ")
    print()


# Pattern 4: Square Pattern with Same Numbers
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

for i in range(1, 5):
    for j in range(4):
        print(i, end=" ")
    print()


# Pattern 5: Pyramid of Stars
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 6: Hourglass Pattern
# * * * * * * *
#   * * * * *
#     * * *
#       *
#     * * *
#   * * * * *
# * * * * * * *

n = 4
for i in range(1, n+1):
    for k in range(1, i):
        print(" ", end=" ")

    for j in range(1, 2 * (n - i) + 2):
        print("*", end=" ")
    print()
for i in range(1, n):
    for k in range(1, n - i):
        print(" ", end=" ")
    for j in range(1, 2*i+2):
        print("*", end=" ")
    print()

# ---------OR---------
n = 4
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

for i in range(2, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

# Pattern 7: Butterfly Pattern
# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *

# Method 1
loop = 1
for i in range(1, 10):
    if i <= 4:
        for j in range(1, i + 1):
            print("*", end=" ")

        for k in range(1, 10-2*i):
            print(" ", end=" ")

        for j in range(1, i + 1):
            print("*", end=" ")

    if i == 5:
        for j in range(1, 10):
            print("*", end=" ")

    if i > 5:
        for j in range(0, i - 2 * loop):
            print("*", end=" ")

        for k in range(0, 2 * loop - 1):
            print(" ", end=" ")

        for j in range(0, i - 2 * loop):
            print("*", end=" ")
        loop = loop + 1
    print()

# Method 2
n = 5  # Total rows in half (top or bottom)
# Top half (1 to 5)
for i in range(1, n + 1):
    # Left wing
    for j in range(1, i + 1):
        print("*", end=" ")

    for k in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()

# Bottom half (4 to 1)
for i in range(n - 1, 0, -1):

    for j in range(1, i + 1):
        print("*", end=" ")

    for k in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()

# Pattern 8: Hollow Butterfly Pattern
# *       *       *
# * *     *     * *
# *   *   *   *   *
# *     * * *     *
# *   *   *   *   *
# * *     *     * *
# *       *       *
n = 3
# Top Half
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    spaces = 2 * (n - i)
    print("  " * spaces, end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Bottom Half
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    spaces = 2 * (n - i)
    print("  " * spaces, end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
