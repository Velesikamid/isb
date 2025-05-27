import json
import argparse


def load_settings() -> dict:
    """
    Loads the settings from a JSON configuration file.
    
    :return: Dictionary containing configuration settings.
    :raises SystemExit: If the settings.json file is not found.
    """
    try:
        with open("settings.json") as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] File settings.json is not found.")
        exit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hybrid cryptosystem")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-gen", "--generation", action="store_true", help="Key generation")
    group.add_argument("-enc", "--encryption", action="store_true", help="Data encryption")
    group.add_argument("-dec", "--decryption", action="store_true", help="Data decryption")
    return parser.parse_args()