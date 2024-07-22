def calculate_trapped_water(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - heights[i]

    return water_trapped

# Test
heights = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0]
print(f"{calculate_trapped_water(heights)}m³")
