import os
import json

def load_post_ids():
    base_dir = os.path.dirname(__file__)  # tests/
    data_path = os.path.join(base_dir, 'data', 'testdata.json')

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found: {data_path}")

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [item["post_id"] for item in data]


    # try:
    #     with open('post_ids.json', 'r') as file:
    #         post_ids = json.load(file)
    #         return post_ids
    # except FileNotFoundError:
    #     return []  # Return an empty list if the file does not exist
    # except json.JSONDecodeError:
    #     return []  # Return an empty list if the JSON is invalid