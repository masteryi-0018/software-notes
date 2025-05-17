#include <iostream>
// #include <stdexcept> // 可以不添加
#include <cassert>

double divide(double numerator, double denominator) {
    assert(denominator != 0 && "Denominator must not be zero!");
    if (denominator == 0) {
        throw std::runtime_error("Division by zero!");
    }
    return numerator / denominator;
}

int main() {
    try {
        double result = divide(10, 2);
        std::cout << "Result: " << result << std::endl;

        result = divide(5, 0); // 这将抛出异常
        std::cout << "This won't be printed" << std::endl;
    }
    catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    catch (...) {
        std::cerr << "Unknown error occurred" << std::endl;
    }

    return 0;
}