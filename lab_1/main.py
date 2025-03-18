import task_1.encryption as t1
import task_2.decryption as t2
from tools.work_with_files import read_json


def main():
    settings = read_json("settings.json")
    encryption_settings = read_json(settings["encryption_settings"])
    decryption_settings = read_json(settings["decryption_settings"])
    t1.encrypt(settings["alphabet"], encryption_settings["in_filename"], encryption_settings["out_filename"], encryption_settings["key"])
    t1.decrypt(settings["alphabet"], encryption_settings["out_filename"], encryption_settings["result_filename"], encryption_settings["key"])
    t2.decrypt(decryption_settings["frequencies_filename"], decryption_settings["in_filename"], decryption_settings["out_filename"], decryption_settings["key"])


if __name__ == "__main__":
    main()