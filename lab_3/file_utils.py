import os
from typing import List


def read_file(path: str) -> bytes:
    """
    Reads binary data from the specified file path.

    :param path: Path to the file to be read.
    :returns: Contents of the file as bytes.
    """
    with open(path, 'rb') as file:
        return file.read()


def write_file(path: str, data: bytes) -> None:
    """
    Writes binary data to the specified file path.

    :param path: Path to the file where data should be written.
    :param data: Data to write to the file.
    """
    with open(path, 'wb') as file:
        file.write(data)


def ensure_exists(paths: List[str]) -> None:
    """
    Checks whether all specified file paths exist.
    Terminates the program if any of the files is missing.

    :param paths: List of file paths to check.
    :raises SystemExit: If any file does not exist.
    """
    for path in paths:
        if not os.path.exists(path):
            print(f"[!] File not found: {path}")
            exit(1)