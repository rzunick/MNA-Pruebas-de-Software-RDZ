# file_operations
import json

def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def generate_id(filename):
    data = read_data_from_file(filename)
    if not data:
        return 1
    else:
        ids = [int(item['id']) for item in data]
        return max(ids) + 1
