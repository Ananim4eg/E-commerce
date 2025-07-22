import json
import os

PATH_TO_JSON_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")


def read_json_file(path_file: str = PATH_TO_JSON_FILE) -> list[dict] | str:
    """Считывает json-файл и возвращает список словарей"""

    try:
        with open(path_file, encoding="utf-8") as settings:
            result: str = json.load(settings)

    except FileNotFoundError:
        return "Ошибка чтения файла."

    return result