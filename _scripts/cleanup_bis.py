import json
import glob
import os

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def remove_matching_strings(reference_data, data):
    if isinstance(data, dict):
        return {
            k: remove_matching_strings(reference_data.get(k, ""), v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [remove_matching_strings(reference_data, item) for item in data]
    elif isinstance(data, str) and data == reference_data:
        return ""
    else:
        return data

def process_json_file(reference_data, file_path):
    data = load_json(file_path)

    cleaned_data = remove_matching_strings(reference_data, data)

    save_json(file_path, cleaned_data)

    print(f"Matching strings removed and saved to {file_path}")

def main():
    reference_file = "gb.json"
    input_dir = "./locales/"

    reference_data = load_json(input_dir + reference_file)

    json_files = glob.glob(input_dir + "*.json")

    for input_file in json_files:
        process_json_file(reference_data, input_file)

if __name__ == "__main__":
    main()
