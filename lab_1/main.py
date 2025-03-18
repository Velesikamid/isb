"""
Main module for performing encryption and decryption tasks based on settings.
"""

import task_1.encryption as t1
import task_2.decryption as t2
from tools.work_with_files import read_json


def main() -> None:
    """
    Main function to execute the encryption and decryption process.

    This function reads settings from a JSON file, performs encryption using
    the specified parameters, and then performs decryption on the encrypted
    text and another set of data using frequency analysis.

    :raises FileNotFoundError: If any of the required JSON files are not found.
    :raises json.JSONDecodeError: If any of the JSONs contain invalid data.
    :raises KeyError: If expected keys are missing in the settings JSON.
    """
    settings = read_json("settings.json")
    encryption_settings = read_json(settings["encryption_settings"])
    decryption_settings = read_json(settings["decryption_settings"])

    t1.encrypt(
        settings["alphabet"],
        encryption_settings["in_filename"],
        encryption_settings["out_filename"],
        encryption_settings["key"]
    )

    t1.decrypt(
        settings["alphabet"],
        encryption_settings["out_filename"],
        encryption_settings["result_filename"],
        encryption_settings["key"]
    )

    t2.decrypt(
        decryption_settings["frequencies_filename"],
        decryption_settings["in_filename"],
        decryption_settings["out_filename"],
        decryption_settings["key"]
    )


if __name__ == "__main__":
    main()
