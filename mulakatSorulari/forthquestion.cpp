#include <iostream>
#include <vector>
#include <algorithm>

int calculate_trapped_water(const std::vector<int>& heights) {
    if (heights.empty()) return 0;

    int n = heights.size();
    std::vector<int> left_max(n), right_max(n);
    int water_trapped = 0;

    left_max[0] = heights[0];
    for (int i = 1; i < n; ++i) {
        left_max[i] = std::max(left_max[i - 1], heights[i]);
    }

    right_max[n - 1] = heights[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        right_max[i] = std::max(right_max[i + 1], heights[i]);
    }

    for (int i = 0; i < n; ++i) {
        water_trapped += std::min(left_max[i], right_max[i]) - heights[i];
    }

    return water_trapped;
}

int main() {
    std::vector<int> heights = {0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0};
    std::cout << calculate_trapped_water(heights) << "m³" << std::endl;
    return 0;
}
