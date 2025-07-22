a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(bin(a)) # bin() function gives the bianry value
print(bin(b))
# Bitwise AND
print("a & b:", a & b)       # 1010 & 0100 = 0000 → 0

# Bitwise OR
print("a | b:", a | b)       # 1010 | 0100 = 1110 → 14

# Bitwise XOR
print("a ^ b:", a ^ b)       # 1010 ^ 0100 = 1110 → 14

# Bitwise NOT
print("~a:", ~a)             # ~10 = -11 (inverts all bits)

# Left Shift
print("a << 1:", a << 1)     # 1010 << 1 = 10100 → 20

# Right Shift
print("a >> 1:", a >> 1)     # 1010 >> 1 = 0101 → 5
