from json import load, dump


def read_json(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        return load(file)


def write_to_json(dictionary: dict, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        dump(dictionary, file, ensure_ascii=False, indent=4)


def read_txt(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    

def write_to_txt(filename: str, data: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)