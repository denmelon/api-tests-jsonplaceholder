import pytest
import requests
from jsonschema import validate
from tests.schemas import post_creation_schema

@pytest.mark.positive
def test_create_post(base_url):
    payload = {
        "title": "Test tile",
        "body": "This is a test body",
        "userId": 1
    }
    headers =  {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post(f"{base_url}/posts", json=payload, headers=headers)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    data = response.json()
    # for key in payload:
    #     assert key in data, f"Response is missing '{key}' field"
    #     assert data[key] == payload[key], f"Expected {key} to be {payload[key]}, got {data[key]}"
    validate(instance=data, schema=post_creation_schema)

@pytest.mark.positive
def test_update_post(base_url):
    post_id = 1
    updated_payload = {
        "id": post_id,
        "title": "Updated title",
        "body": "Updated body content",
        "userId": 1
    }
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.put(f"{base_url}/posts/{post_id}", json=updated_payload, headers=headers)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    for key in updated_payload:
        assert key in data, f"Response is missing '{key}' field"
        assert data[key] == updated_payload[key], f"Expected {key} to be {updated_payload[key]}, got {data[key]}"

@pytest.mark.positive
def test_delete_post(base_url):
    post_id = 1
    response = requests.delete(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json() == {}, f"Expected response is empty, got {response.json()}"
