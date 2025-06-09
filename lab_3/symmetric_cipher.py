from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_pad
import os


def encrypt(data: bytes, key: bytes) -> bytes:
    """Encrypt data using SEED algorithm in CBC mode with ANSIX923 padding.

    :param data: Raw bytes to be encrypted. Length must be compatible with padding
    :param key: Encryption key (16 bytes for SEED-128, 32 bytes for SEED-256)
    :return: Encrypted data in format: IV (16 bytes) + ciphertext
    :raises ValueError: If key length is invalid for SEED algorithm
    :raises TypeError: If input data is not bytes
    """
    if len(key) not in {16, 32}:
        raise ValueError("SEED key must be 16 or 32 bytes long")
    
    padder = sym_pad.ANSIX923(128).padder()
    padded = padder.update(data) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded) + encryptor.finalize()
    return iv + encrypted


def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypt data encrypted with SEED-CBC-ANSIX923.

    :param encrypted_data: Encrypted data in format: IV (16 bytes) + ciphertext
    :param key: Decryption key (same as used for encryption)
    :return: Original decrypted data
    :raises ValueError: If key is invalid or encrypted_data is too short
    :raises TypeError: If inputs are not bytes
    :raises PaddingError: If padding is corrupted
    """
    if len(encrypted_data) < 16:
        raise ValueError("Encrypted data must contain at least 16 bytes (IV)")
    if len(key) not in {16, 32}:
        raise ValueError("SEED key must be 16 or 32 bytes long")

    iv = encrypted_data[:16]
    content = encrypted_data[16:]
    cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(content) + decryptor.finalize()
    unpadder = sym_pad.ANSIX923(128).unpadder()
    return unpadder.update(decrypted_padded) + unpadder.finalize()