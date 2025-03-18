from tools.work_with_files import read_txt, write_to_txt


def encrypt(alphabet: str, in_filename: str, out_filename: str, key: str) -> None:
    text = read_txt(in_filename)
    result = ""
    for i in range(len(text)):
        char = text[i].upper()
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + alphabet.index(key[i % len(key)])) % len(alphabet)]
        else:
            result += char
    write_to_txt(out_filename, result)


def decrypt(alphabet: str, in_filename: str, out_filename: str, key: str) -> None:
    ciphertext = read_txt(in_filename)
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i].upper()
        if char in alphabet:
            result += alphabet[(alphabet.index(char) - alphabet.index(key[i % len(key)])) % len(alphabet)]
        else:
            result += char
    write_to_txt(out_filename, result)
    