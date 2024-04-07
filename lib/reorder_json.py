import json, json5
from collections import OrderedDict


def sort_json(obj):
    if isinstance(obj, dict):
        return OrderedDict(sorted((k, sort_json(v)) for k, v in obj.items()))
    if isinstance(obj, list):
        return [sort_json(x) for x in obj]
    else:
        return obj


def reorder_settings(input_file_path, output_file_path):
    with open(input_file_path) as f:
        data = json5.load(f)
    ordered_data = sort_json(data)
    with open(output_file_path, "w") as f:
        json.dump(ordered_data, f, indent=4, ensure_ascii=False)


reorder_settings(
    "/Users/gaojian15/Library/Application Support/Code/User/settings.json",
    "output.json",
)
