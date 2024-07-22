#include <iostream>
#include <vector>
#include <string>

std::pair<std::vector<int>, int> count_and_list_threes(int n) {
    int count = 0;
    std::vector<int> numbers_with_threes;
    for (int i = 0; i <= n; ++i) {
        std::string num = std::to_string(i);
        int temp_count = 0;
        for (char c : num) {
            if (c == '3') {
                temp_count++;
            }
        }
        if (temp_count > 0) {
            numbers_with_threes.push_back(i);
            count += temp_count;
        }
    }
    return {numbers_with_threes, count};
}

int main() {
    int n = 37;
    auto result = count_and_list_threes(n);
    std::cout << "[";
    for (size_t i = 0; i < result.first.size(); ++i) {
        std::cout << result.first[i];
        if (i != result.first.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "], " << result.second << " Adet 3 kullanılmıştır." << std::endl;
    return 0;
}
