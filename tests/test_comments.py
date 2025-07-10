import pytest
import requests
from jsonschema import validate
from tests.schemas import comment_schema

@pytest.mark.positive
def test_get_all_comments(base_url):
    response = requests.get(f"{base_url}/comments")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert isinstance(data, list), f"Expected data type list, got {type(data)}"
    assert len(data) > 0, f"Expected data size > 0, got {len(data)}"

    for item in data:
        validate(instance=item, schema=comment_schema)