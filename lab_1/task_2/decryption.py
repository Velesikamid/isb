"""
Module for frequency analysis and substitution cipher decryption.
"""

from collections import Counter

from tools.work_with_files import *


def analyze_frequency(text: str, frequencies_filename: str) -> None:
    """
    Analyzes character frequency in text and saves sorted results to JSON.

    :param text: Input text for frequency analysis
    :param frequencies_filename: Output JSON filename for frequencies
    :raises FileNotFoundError: If output file path is invalid
    :raises PermissionError: If no write permissions for output file
    """
    counter = Counter(char for char in text)
    total = len(text)
    frequencies = {char: count / total for char, count in counter.items()}
    write_to_json(dict(sorted(frequencies.items(),
                              key=lambda item: item[1],
                              reverse=True)),
                  frequencies_filename)


def decrypt(frequences_filename: str,
            in_filename: str,
            out_filename: str,
            key_filename: str) -> None:
    """
    Decrypts text using substitution cipher based on frequency analysis key.

    :param frequences_filename: JSON file to store ciphertext frequencies
    :param in_filename: Input file with encrypted text
    :param out_filename: Output file for decrypted text
    :param key_filename: JSON file with substitution mapping
    :raises FileNotFoundError: If any input file is missing
    :raises json.JSONDecodeError: If key file contains invalid JSON
    """
    ciphertext = read_txt(in_filename)
    analyze_frequency(ciphertext, frequences_filename)

    key = read_json(key_filename)
    result = "".join(key.get(char, char) for char in ciphertext)
    write_to_txt(out_filename, result)
