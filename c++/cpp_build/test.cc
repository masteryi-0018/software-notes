#include "add.h"

#include <iostream>

int main() {
	int a = 1;
	int b = 2;
	int c = add(a, b);
	std::cout << c << std::endl;
	int* p = nullptr;
	*p = 42;
	return 0;
}