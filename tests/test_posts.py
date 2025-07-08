import pytest
import requests

from tests.conftest import load_post_ids


def test_get_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

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


@pytest.mark.parametrize("post_id", load_post_ids(), ids=lambda val: f"id={val}")
def test_get_single_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # check if the response has the required fields
    data = response.json()
    assert data["id"] == post_id, f"Expected post id {post_id}, got {data['id']}"
    assert "title" in data, "Post is missing 'title' field"
    assert "body" in data, "Post is missing 'body' field"