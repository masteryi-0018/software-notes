#include <iostream>
#include <chrono>
#include <vector>

const long int N = 100000000;

void test_1() {
    int a = 0;
    int sum = 0;
    while (std::cin >> a) {
         sum += a;
    }
    std::cout << sum << std::endl;
    return;
}


void test_post_increment() {
    std::vector<int> v(N, 1);
    volatile int sum = 0; // 防止优化
    auto start = std::chrono::high_resolution_clock::now();

    for (auto it = v.begin(); it != v.end(); it++) { // it++ 后缀自增
        sum += *it;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Post-increment (it++) time: "
              << std::chrono::duration<double>(end - start).count()
              << " s, sum=" << sum << std::endl;
}

void test_pre_increment() {
    std::vector<int> v(N, 1);
    volatile int sum = 0; // 防止优化
    auto start = std::chrono::high_resolution_clock::now();

    for (auto it = v.begin(); it != v.end(); ++it) { // ++it 前缀自增
        sum += *it;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Pre-increment (++it) time: "
              << std::chrono::duration<double>(end - start).count()
              << " s, sum=" << sum << std::endl;
}

void test_2() {
    test_post_increment();
    test_pre_increment();
}

int main() {
    // test_1();
    test_2();

    return 0;
}