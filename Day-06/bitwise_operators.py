# Bitwise Operators in Python

# Let's define two numbers
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(f"a = {a} -> binary: {bin(a)}")
print(f"b = {b} -> binary: {bin(b)}")

# 1. Bitwise AND (&)
print("\n1️⃣ Bitwise AND (&)")
print(f"a & b = {a & b} -> binary: {bin(a & b)}")
# 1010 & 0100 = 0000 0100 = 4

# 2. Bitwise OR (|)
print("\n2️⃣ Bitwise OR (|)")
print(f"a | b = {a | b} -> binary: {bin(a | b)}")
# 1010 | 0100 = 1110 = 14

# 3. Bitwise XOR (^)
print("\n3️⃣ Bitwise XOR (^)")
print(f"a ^ b = {a ^ b} -> binary: {bin(a ^ b)}")
# 1010 ^ 0100 = 1110 = 14

# 4. Bitwise NOT (~)
print("\n4️⃣ Bitwise NOT (~)")
print(f"~a = {~a} -> binary: {bin(~a)}")
# ~1010 = -(1010 + 1) = -11

# 5. Left Shift (<<)
print("\n5️⃣ Left Shift (<<)")
print(f"a << 1 = {a << 1} -> binary: {bin(a << 1)}")
# Shifts bits left by 1 (multiply by 2)

# 6. Right Shift (>>)
print("\n6️⃣ Right Shift (>>)")
print(f"a >> 1 = {a >> 1} -> binary: {bin(a >> 1)}")
# Shifts bits right by 1 (divide by 2)
