#include <bitset>
#include <iostream>
#include <random>

std::bitset<128> generate_random_binary_sequence() {
    std::random_device rd;
    std::mt19937_64 gen(rd());
    std::uniform_int_distribution<uint64_t> dist(0, UINT64_MAX);

    uint64_t part1 = dist(gen);
    uint64_t part2 = dist(gen);

    std::bitset<128> result(part1);
    result <<= 64;
    result |= part2;

    return result;
}

int main() {
    std::bitset<128> random_sequence = generate_random_binary_sequence();
    std::cout << "Random 128-bit binary sequence: " << random_sequence << std::endl;
    return 0;
}