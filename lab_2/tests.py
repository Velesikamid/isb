"""Statistical tests for random binary sequences.

This module implements NIST-style randomness tests for binary sequences:
- Frequency (monobit) test
- Consecutive bits (runs) test
- Longest run of ones in a block test
"""

import math
from scipy.special import gammainc
from tools.work_with_files import read_json


def frequency_bitwise_test(sequence: str) -> float:
    """Perform frequency (monobit) test on binary sequence.

    Computes the proportion of ones versus zeros in the sequence.
    A truly random sequence should have approximately equal counts.

    Args:
        sequence: Binary string (e.g. "010110...").

    Returns:
        P-value from the normal distribution ERFC function.
        Values close to 0 indicate non-randomness.
    """
    n = len(sequence)
    s = abs(1 / math.sqrt(n) * (sequence.count("1") - sequence.count("0")))
    return math.erfc(s / math.sqrt(2))


def consecutive_bits_test(sequence: str) -> float:
    """Perform runs test on binary sequence.

    Counts the number of transitions between 0 and 1.
    Too few or too many transitions suggest non-randomness.

    Args:
        sequence: Binary string to analyze.

    Returns:
        P-value. Returns 0 if the sequence is clearly biased
        (proportion of ones differs significantly from 0.5).
    """
    n = len(sequence)
    p = sequence.count("1") / n
    if abs(p - 0.5) >= 2 / math.sqrt(n):
        return 0

    v = sum(sequence[i] != sequence[i + 1] for i in range(n - 1))
    return math.erfc(
        abs(v - 2 * n * p * (1 - p)) / (2 * math.sqrt(2 * n) * p * (1 - p))
    )


def longest_sequence_of_units_test(sequence: str) -> float:
    """Perform longest run of ones in 8-bit blocks test.

    Splits the sequence into 8-bit blocks and analyzes
    the distribution of the longest runs of ones.

    Args:
        sequence: Binary string to test.

    Returns:
        P-value from the chi-squared test with 3 degrees of freedom.
    """
    c = read_json("constants.json")
    n = len(sequence)
    v = [0, 0, 0, 0]

    for i in range(0, n, 8):
        max_length = 0
        current_length = 0
        for j in sequence[i:i + 8]:
            if j == "1":
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0

        match max_length:
            case 0 | 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1

    he2 = sum((v[i] - 16 * c["PI"][i])**2 / (16 * c["PI"][i]) for i in range(4))
    return gammainc(3 / 2, he2 / 2)


def save_results_to_file(fr: float, cb: float, ls: float, path: str) -> None:
    """Save test results to specified file path.

    Args:
        fr: P-value from frequency test.
        cb: P-value from runs test.
        ls: P-value from longest run test.
        path: Output file path.
    """
    try:
        with open(path, "a") as file:
            print(f"Pvalue of Frequency bitwise test: {fr}", file=file)
            print(f"Pvalue of Test for identical consecutive bits: {cb}", file=file)
            print("Pvalue of Test for the longest sequence " +
                  f"of units in a block: {ls}", file=file)
            print("", file=file)
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Execute all tests on predefined sequences and save results."""
    rs = read_json("random_sequences/random_sequences.json")
    c = read_json("constants.json")

    fr_cpp = frequency_bitwise_test(rs["CPP"])
    cb_cpp = consecutive_bits_test(rs["CPP"])
    ls_cpp = longest_sequence_of_units_test(rs["CPP"])
    save_results_to_file(fr_cpp, cb_cpp, ls_cpp, c["OUTPUT"])

    fr_java = frequency_bitwise_test(rs["JAVA"])
    cb_java = consecutive_bits_test(rs["JAVA"])
    ls_java = longest_sequence_of_units_test(rs["JAVA"])
    save_results_to_file(fr_java, cb_java, ls_java, c["OUTPUT"])


if __name__ == "__main__":
    main()
