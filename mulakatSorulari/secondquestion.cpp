#include <iostream>

int add(int a, int b) {
    while (b != 0) {
        int carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

int main() {
    int num1 = 27;
    int num2 = 27;
    std::cout << "Toplam: " << add(num1, num2) << std::endl;
    return 0;
}
