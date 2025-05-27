#include <bitset>
#include <iostream>
#include <random>

/**
 * @brief Generates a random 128-bit binary sequence
 * 
 * This function generates a uniformly distributed random 128-bit binary sequence
 * using the Mersenne Twister algorithm for random number generation.
 * 
 * @return std::bitset<128> A bitset containing the generated 128-bit sequence
 */
std::bitset<128> generateRandomBinarySequence() 
{
    std::random_device rd;  // True random number generator for seeding
    std::mt19937_64 gen(rd());  // Mersenne Twister 64-bit RNG
    std::uniform_int_distribution<uint64_t> dist(0, UINT64_MAX);  // Uniform distribution

    // Generate two 64-bit random numbers
    uint64_t part1 = dist(gen);
    uint64_t part2 = dist(gen);

    // Combine into 128-bit bitset
    std::bitset<128> result(part1);
    result <<= 64;
    result |= part2;

    return result;
}

/**
 * @brief Main function demonstrating the binary sequence generator
 * 
 * Generates and prints a random 128-bit binary sequence to standard output.
 * 
 * @return int Returns 0 on successful execution
 */
int main() 
{
    std::bitset<128> randomSequence = generateRandomBinarySequence();
    std::cout << "Random 128-bit binary sequence: " << randomSequence << std::endl;
    return 0;
}