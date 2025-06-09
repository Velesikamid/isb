import argparse
import json
from typing import Any, Dict


def load_config() -> Dict[str, Any]:
    """
    Loads configuration settings from the 'settings.json' file.

    :returns: A dictionary containing configuration settings.
    :raises SystemExit: If the file 'settings.json' is not found.
    """
    try:
        with open('settings.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] settings.json file not found.")
        exit(1)


def get_args() -> argparse.Namespace:
    """
    Parses command-line arguments for hybrid cryptosystem operations.

    :returns: Parsed command-line arguments as a namespace object.
    """
    parser = argparse.ArgumentParser(description="Hybrid Cryptosystem")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('-gen', '--create_keys', action='store_true', help='Generate keys')
    mode.add_argument('-enc', '--encrypt', action='store_true', help='Encrypt data')
    mode.add_argument('-dec', '--decrypt', action='store_true', help='Decrypt data')
    return parser.parse_args()