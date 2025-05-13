"""
Module for working with JSON and TXT files.
"""

from json import load, dump


def read_json(filename: str) -> dict:
    """
    Reads data from a JSON file.

    :param filename: Name of the file to read.
    :return: Dictionary with data from the file.
    :raises FileNotFoundError: If the file is not found.
    :raises json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return load(file)
    except Exception as e:
        print(f"Error: {e}")


def write_to_json(dictionary: dict, filename: str) -> None:
    """
    Writes a dictionary to a JSON file.

    :param dictionary: Dictionary to write to the file.
    :param filename: Name of the file to write.
    :raises TypeError: If a non-dictionary is passed.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            dump(dictionary, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error: {e}")


def read_txt(filename: str) -> str:
    """
    Reads the contents of a TXT file.

    :param filename: Name of the file to read.
    :return: String with the file contents.
    :raises FileNotFoundError: If the file is not found.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error: {e}")


def write_to_txt(filename: str, data: str) -> None:
    """
    Writes a string to a TXT file.

    :param filename: Name of the file to write.
    :param data: String to write to the file.
    :raises TypeError: If a non-string is passed.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as e:
        print(f"Error: {e}")
