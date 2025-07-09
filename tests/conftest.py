# import os
import pytest
import json
from pathlib import Path

# fixture with session scope to provide the base URL for the API
@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

# fixture to load post IDs from a JSON file
def load_test_data():
    base_dir = Path(__file__).parent  # tests/
    data_path = base_dir / 'data' / 'testdata.json'

    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    with data_path.open('r', encoding='utf-8') as f:
        data = json.load(f)
        return [(item["post_id"], item["expected_status"]) for item in data]




# def load_post_ids():
#     base_dir = os.path.dirname(__file__)  # tests/
#     data_path = os.path.join(base_dir, 'data', 'testdata.json')
#
#     if not os.path.exists(data_path):
#         raise FileNotFoundError(f"Data file not found: {data_path}")
#
#     with open(data_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         return [item["post_id"] for item in data]

