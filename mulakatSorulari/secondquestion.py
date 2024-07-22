def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test
num1 = 27
num2 = 27
print(f"Toplam: {add(num1, num2)}")
