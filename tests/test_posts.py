import pytest
import requests
from jsonschema import validate
from tests.conftest import load_test_data
from tests.schemas import post_schema

@pytest.mark.smoke
def test_get_all_posts(base_url):
    # url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(f"{base_url}/posts")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    #check if the response is a list
    data = response.json()
    assert isinstance(data, list), f"Expected data type list, got {type(data)}"
    assert len(data) > 0, f"Expected 1 data item, got {len(data)}"

    # Check if each post has the required fields
    for post in data:
        assert "userId" in post, "Post is missing 'userId' field"
        assert "id" in post, "Post is missing 'id' field"
        assert "title" in post, "Post is missing 'title' field"
        assert "body" in post, "Post is missing 'body' field"

# filter positive cases with status code 200
positive_test_data = [t for t in load_test_data() if t[1] == 200]

@pytest.mark.positive
@pytest.mark.parametrize("post_id, expected_status", positive_test_data, ids=lambda val: f"id={val}")
def test_get_existing_post(base_url, post_id, expected_status):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == expected_status, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    validate(instance=data, schema=post_schema) # validate the response against the schema
    assert data["id"] == post_id, f"Expected post id {post_id}, got {data['id']}"

@pytest.mark.positive
@pytest.mark.parametrize("post_id, expected_status", positive_test_data, ids=lambda val: f"id={val}")
def test_get_single_post(base_url, post_id, expected_status):
    # url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(f"{base_url}/posts/{post_id}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == expected_status, f"Expected status code 200, got {response.status_code}"

    # check if the response has the required fields
    if expected_status == 200:
        data = response.json()
        assert data["id"] == post_id, f"Expected post id {post_id}, got {data['id']}"
        assert "title" in data, "Post is missing 'title' field"
        assert "body" in data, "Post is missing 'body' field"


# filter negative cases with status code not 200
negative_test_data = [t for t in load_test_data() if t[1] != 200]

@pytest.mark.negative
@pytest.mark.parametrize("post_id, expected_status", negative_test_data, ids=lambda val: f"id={val}")
def test_get_nonexistent_post(base_url, post_id, expected_status):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == expected_status, f"Expected status code not 200, got {response.status_code}"
