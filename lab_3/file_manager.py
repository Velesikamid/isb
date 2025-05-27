import os
from cryptography.hazmat.primitives import serialization


class FileManager:
    def check_files_exist(paths: list) -> None:
        """
        Checks whether the specified files exist.
        
        :param paths: List of file paths to check.
        :raises SystemExit: If any file is not found.
        """
        for path in paths:
            if not os.path.exists(path):
                print(f"[!] File is not found: {path}")
                exit(1)
    

    def save_public_key(filename: str, public_key) -> None:
        with open(filename, "wb") as file:
            file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))