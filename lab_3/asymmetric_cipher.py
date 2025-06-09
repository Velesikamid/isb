import os
from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey
from cryptography.hazmat.primitives import serialization, hashes


def generate_rsa_keypair() -> Tuple[RSAPrivateKey, RSAPublicKey]:
    """
    Generates a new RSA private-public key pair.

    :returns: A tuple containing the RSA private key and corresponding public key.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()


def encrypt(key: bytes, public_key: RSAPublicKey) -> bytes:
    """
    Encrypts data using the given RSA public key with OAEP padding.

    :param key: Symmetric key or data to encrypt.
    :param public_key: RSA public key used for encryption.
    :returns: Encrypted data as bytes.
    """
    return public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def decrypt(encrypted_key: bytes, private_key: RSAPrivateKey) -> bytes:
    """
    Decrypts data using the given RSA private key with OAEP padding.

    :param encrypted_key: Encrypted data to decrypt.
    :param private_key: RSA private key used for decryption.
    :returns: Decrypted data as bytes.
    """
    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def serialize_public_key(public_key: RSAPublicKey) -> bytes:
    """
    Serializes an RSA public key to PEM format.

    :param public_key: RSA public key to serialize.
    :returns: Serialized public key in PEM format.
    """
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


def serialize_private_key(private_key: RSAPrivateKey) -> bytes:
    """
    Serializes an RSA private key to PEM format without encryption.

    :param private_key: RSA private key to serialize.
    :returns: Serialized private key in PEM format.
    """
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )


def load_private_key(data: bytes) -> RSAPrivateKey:
    """
    Loads an RSA private key from PEM-encoded data.

    :param data: PEM-encoded private key bytes.
    :returns: Deserialized RSA private key object.
    """
    return serialization.load_pem_private_key(data, password=None)