import json
import os

def read_json_file(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None

    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file) 