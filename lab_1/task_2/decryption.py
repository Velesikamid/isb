from collections import Counter

from tools.work_with_files import write_to_json, read_json, read_txt, write_to_txt

def analyze_frequency(text: str, frequencies_filename: str) -> None:
    counter = Counter(char for char in text)
    total = len(text)
    frequencies = {char: count / total for char, count in counter.items()}
    write_to_json(dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True)), frequencies_filename)


def decrypt(frequences_filename: str, in_filename: str, out_filename: str, key_filename: str):
    ciphertext = read_txt(in_filename)
    analyze_frequency(ciphertext, frequences_filename)

    key = read_json(key_filename)
    result = "".join(key.get(char, char) for char in ciphertext)
    write_to_txt(out_filename, result)
