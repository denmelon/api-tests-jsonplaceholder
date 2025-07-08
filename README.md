
# 🔗 API Tests – JSONPlaceholder

Тесты для бесплатного API: https://jsonplaceholder.typicode.com

## 🔍 Что проверяем

- `GET /posts` – список всех постов
- Позитивные и негативные кейсы
- JSON-валидация и статус-коды
- HTML-отчёты с помощью `pytest-html`

## 🗂 Структура проекта

```
api-tests-jsonplaceholder/
├── data/
│   └── testdata.json
├── tests/
│   └── test_posts.py
├── conftest.py
├── run_tests.py
├── requirements.txt
├── reports/
│   └── report.html
├── README.md
```

## ▶️ Запуск тестов

Создание HTML-отчёта:

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

Автоматический запуск с открытием отчёта:

```bash
python run_tests.py
```

## 🛠 Требования

```txt
requests
pytest
pytest-html
```

## 📁 Пример структуры JSON

`data/testdata.json`:

```json
[
  { "post_id": 1 },
  { "post_id": 100 },
  { "post_id": 9999 }
]
```
