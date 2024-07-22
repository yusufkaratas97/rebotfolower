def count_and_list_threes(n):
    count = 0
    numbers_with_threes = []
    for i in range(n + 1):
        if '3' in str(i):
            numbers_with_threes.append(i)
            count += str(i).count('3')
    return numbers_with_threes, count

# Test
n = 37
numbers_with_threes, count = count_and_list_threes(n)
print(f"{numbers_with_threes}, {count} Adet 3 kullanılmıştır.")
