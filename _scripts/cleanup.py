import json
import glob
import os

def remove_empty_strings(data):
    if isinstance(data, dict):
        return {k: remove_empty_strings(v) for k, v in data.items() if v != ""}
    elif isinstance(data, list):
        return [remove_empty_strings(item) for item in data if item != ""]
    else:
        return data

def process_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cleaned_data = remove_empty_strings(data)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

    print(f"Empty strings removed and saved to {file_path}")

def main():
    input_dir = "./locales/"

    json_files = glob.glob(input_dir + "*.json")

    for input_file in json_files:
        process_json_file(input_file)

if __name__ == "__main__":
    main()
