import helpers
import file_utils
import asymmetric_cipher
import symmetric_cipher
import os
from typing import Dict, Any


def create_keys(config: Dict[str, Any]) -> None:
    """
    Generates a symmetric AES key and an RSA key pair, encrypts the symmetric key
    with the RSA public key, and saves all keys to files.

    :param config: Configuration dictionary containing the path to store the encrypted symmetric key.
    """
    print("[*] Generating keys...")
    sym_key = os.urandom(16)
    priv_key, pub_key = asymmetric_cipher.generate_rsa_keypair()
    encrypted_sym_key = asymmetric_cipher.encrypt(sym_key, pub_key)

    file_utils.write_file("rsa_pub_key.txt", asymmetric_cipher.serialize_public_key(pub_key))
    file_utils.write_file("rsa_private_key.txt", asymmetric_cipher.serialize_private_key(priv_key))
    file_utils.write_file(config['encoded_sym_key'], encrypted_sym_key)

    print("[+] Keys successfully generated.")


def encrypt_data(config: Dict[str, Any]) -> None:
    """
    Encrypts plaintext data using a symmetric key that is decrypted from a previously
    RSA-encrypted file. Saves the encrypted result to a file.

    :param config: Configuration dictionary containing paths to the RSA private key,
                   encrypted symmetric key, plaintext input, and encrypted output.
    """
    print("[*] Loading data for encryption...")
    file_utils.ensure_exists([config['rsa_private'], config['encoded_sym_key'], config['plain_data']])

    private_key = asymmetric_cipher.load_private_key(file_utils.read_file(config['rsa_private']))
    sym_key = asymmetric_cipher.decrypt(file_utils.read_file(config['encoded_sym_key']), private_key)
    plaintext = file_utils.read_file(config['plain_data'])
    encrypted = symmetric_cipher.encrypt(plaintext, sym_key)

    file_utils.write_file(config['encrypted_data'], encrypted)
    print("[+] Data encrypted successfully.")


def decrypt_data(config: Dict[str, Any]) -> None:
    """
    Decrypts encrypted data using a symmetric key that is decrypted from a file
    encrypted with RSA. Saves the decrypted output to a file.

    :param config: Configuration dictionary containing paths to the RSA private key,
                   encrypted symmetric key, encrypted input, and decrypted output.
    """
    print("[*] Loading data for decryption...")
    file_utils.ensure_exists([config['rsa_private'], config['encoded_sym_key'], config['encrypted_data']])

    private_key = asymmetric_cipher.load_private_key(file_utils.read_file(config['rsa_private']))
    sym_key = asymmetric_cipher.decrypt(file_utils.read_file(config['encoded_sym_key']), private_key)
    encrypted_data = file_utils.read_file(config['encrypted_data'])
    decrypted = symmetric_cipher.decrypt(encrypted_data, sym_key)

    file_utils.write_file(config['decrypted_output'], decrypted)
    print("[+] Data decrypted successfully.")


def main() -> None:
    """
    Parses command-line arguments and performs the selected action:
    key generation, encryption, or decryption.
    """
    args = helpers.get_args()
    config = helpers.load_config()

    if args.create_keys:
        create_keys(config)
    elif args.encrypt:
        encrypt_data(config)
    elif args.decrypt:
        decrypt_data(config)


if __name__ == "__main__":
    main()