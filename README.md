# 🧪 API Tests: JSONPlaceholder

Automated API-tests for [JSONPlaceholder](https://jsonplaceholder.typicode.com) using `pytest` and `requests`.

## 📁 Project Structure

```
api-tests-jsonplaceholder/
├── data/
│   └── testdata.json          # Test data: post IDs and expected status
├── reports/
│   └── report.html            # Generated HTML test report
├── tests/
│   ├── conftest.py            # Fixtures and data loaders
│   └── test_posts.py          # Test cases: GET /posts
├── requirements.txt
└── README.md
```

## ✅ Coverage

- `GET /posts` — Retrieve all posts
- `GET /posts/{id}` — Retrieve a single post by ID
- 🟢 Positive cases (200 OK)
- 🔴 Negative cases (404 Not Found)
- 📄 HTML report generation (reports/report.html)

## 🧪 Test Example

```python
@pytest.mark.parametrize("post_id, expected_status", load_test_data(), ids=lambda val: f"id={val[0]}-{val[1]}")
def test_get_single_post(base_url, post_id, expected_status):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()
        assert data["id"] == post_id
```

## ▶️ Running Tests

Install dependencies:
```bash
pip install -r requirements.txt
```

Run all tests with an HTML report:
```bash
pytest --html=reports/report.html
```

Run only positive test cases:
```bash
pytest -m positive --html=reports/positive.html
```

Run only negative test cases:
```bash
pytest -m negative --html=reports/negative.html
```

## 🏷 Markers

- `@pytest.mark.positive` — Positive test cases (valid post IDs)
- `@pytest.mark.negative` — Negative test cases (invalid post IDs)

## 🔧 Fixtures

Fixtures are defined in `conftest.py`:
- `base_url` — the API base URL
- `load_test_data` — loads test cases from `data/testdata.json`
```
## ✅ JSON Schema Validation

Each positive test includes JSON Schema validation using the `jsonschema` library.

Schemas are stored in `tests/schemas.py` and reused across tests to validate structure and required fields in API responses.

## 🛠 Used Technologies

- `pytest` — testing framework
- `requests` — HTTP client for APIs
- `pytest-html` — HTML report generator

---

## 💡 Future Improvements

- Extend coverage to `/comments`, `/users`, etc.
- Add CI via GitHub Actions
- Add negative test coverage for POST, PUT, DELETE

📌 Repository: [GitHub — denmelon/api-tests-jsonplaceholder](https://github.com/denmelon/api-tests-jsonplaceholder)
