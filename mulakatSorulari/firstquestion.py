def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# Test
n = 70
print(f"{n}! sayısının sondan {count_trailing_zeros(n)} basamağı sıfırdır.")
