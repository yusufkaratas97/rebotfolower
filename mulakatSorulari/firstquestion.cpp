#include <iostream>

int count_trailing_zeros(int n) {
    int count = 0;
    while (n >= 5) {
        n /= 5;
        count += n;
    }
    return count;
}

int main() {
    int n = 70;
    std::cout << n << "! sayısının sondan " << count_trailing_zeros(n) << " basamağı sıfırdır." << std::endl;
    return 0;
}
