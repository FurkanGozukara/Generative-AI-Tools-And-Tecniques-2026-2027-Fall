#include <iostream>
#include <numeric>
#include <vector>

int main() {
    const std::vector<int> values{6, 12, 24};
    const int total = std::accumulate(values.begin(), values.end(), 0);
    std::cout << "Week 01 C++ toolchain OK | sum=" << total << '\n';
    return total == 42 ? 0 : 1;
}
