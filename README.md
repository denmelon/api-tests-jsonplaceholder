# 🧪 API Tests: JSONPlaceholder

Automated API-tests for [JSONPlaceholder](https://jsonplaceholder.typicode.com) using `pytest` and `requests`.

## 📁 Структура проекта

```
api-tests-jsonplaceholder/
├── data/
│   └── testdata.json          # Test data: IDs and expected status codes
├── reports/
│   └── report.html            # HTML report with test results
├── tests/
│   └── test_posts.py          # Tests for GET /posts and GET /posts/{id}
├── conftest.py                # Fixtures: base_url, JSON data loader
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## ✅ Что покрыто

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

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests with report:
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

## 🛠 Used Technologies

- `pytest` — testing framework
- `requests` — HTTP client for APIs
- `pytest-html` — HTML report generator

---

📌 Repository: [GitHub — denmelon/api-tests-jsonplaceholder](https://github.com/denmelon/api-tests-jsonplaceholder)