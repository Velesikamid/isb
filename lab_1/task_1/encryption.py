"""
Module for encrypting and decrypting text using a Vigenère cipher.
"""

from tools.work_with_files import read_txt, write_to_txt


def encrypt(alphabet: str,
            in_filename: str,
            out_filename: str,
            key: str) -> None:
    """
    Encrypts a text file using a Vigenère cipher.

    :param alphabet: The alphabet to use for encryption.
    :param in_filename: Name of the input file to encrypt.
    :param out_filename: Name of the output file for the encrypted text.
    :param key: The encryption key.
    :raises FileNotFoundError: If the input file is not found.
    """
    text = read_txt(in_filename)
    result = ""
    for i in range(len(text)):
        char = text[i].upper()
        if char in alphabet:
            result += alphabet[(alphabet.index(char)
                                + alphabet.index(key[i % len(key)]))
                               % len(alphabet)]
        else:
            result += char
    write_to_txt(out_filename, result)


def decrypt(alphabet: str,
            in_filename: str,
            out_filename: str,
            key: str) -> None:
    """
    Decrypts a text file that was encrypted using a Vigenère cipher.

    :param alphabet: The alphabet to use for decryption.
    :param in_filename: Name of the input file to decrypt.
    :param out_filename: Name of the output file for the decrypted text.
    :param key: The decryption key (must be the same as the encryption key).
    :raises FileNotFoundError: If the input file is not found.
    """
    ciphertext = read_txt(in_filename)
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i].upper()
        if char in alphabet:
            result += alphabet[(alphabet.index(char)
                                - alphabet.index(key[i % len(key)]))
                               % len(alphabet)]
        else:
            result += char
    write_to_txt(out_filename, result)
