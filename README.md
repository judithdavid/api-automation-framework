# API Automation Framework

Production-grade API automation framework built using Python, PyTest, and Requests with reusable client architecture, centralized validation, structured logging, schema validation, mocking support, environment-based configuration, and CI-ready design.

---

# Features

- Reusable HTTP client using `requests.Session`
- Retry strategy for transient failures
- Structured logging with request tracing
- Environment-based configuration using `.env`
- Response abstraction layer
- Schema validation using `jsonschema`
- Custom assertion layer
- CRUD API workflow validation
- Positive and negative API testing
- Mocking support using `responses`
- Smoke and regression test tagging
- CI-ready architecture
- Allure reporting support

---

# Tech Stack

- Python 3.12
- PyTest
- Requests
- JsonSchema
- Responses
- Allure PyTest
- Python Dotenv
- GitHub Actions

---

# Framework Architecture

```text
api-automation-framework/
│
├── clients/
│   └── api_client.py
│
├── config/
│   └── config.py
│
├── core/
│   ├── assertions.py
│   └── response.py
│
├── schemas/
│   └── user_schema.py
│
├── tests/
│   ├── test_users.py
│   ├── test_crud_flow.py
│   ├── test_negative.py
│   └── test_mock_users.py
│
├── utils/
│   ├── loggers.py
│   └── validators.py
│
├── logs/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# API Under Test

Public REST API provided by ReqRes:

https://reqres.in

---

# Logging System

The framework supports configurable logging levels through `.env`.

## DEBUG mode

Logs:
- Request URL
- Payload
- Response body
- Response timing
- Request tracing IDs

## INFO mode

Logs:
- Request URL
- Response status
- Response timing

Error responses are always logged.

---

# Test Coverage

The framework currently validates:

- GET users
- CRUD workflow
- Negative endpoint validation
- Schema validation
- Mocked API responses
- Response contract validation

---

# Environment Configuration

Create a `.env` file in the project root:

```env
API_BASE_URL=https://reqres.in/api
API_TIMEOUT=10

API_EMAIL=eve.holt@reqres.in
API_PASSWORD=cityslicka

API_KEY=your_api_key_here

LOG_LEVEL=DEBUG
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd api-automation-framework
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run full suite

```bash
pytest -v
```

---

## Run smoke tests

```bash
pytest -m smoke
```

---

## Run regression tests

```bash
pytest -m regression
```

---

## Run mock tests

```bash
pytest tests/test_mock_users.py -v
```

---

# Allure Reporting

Generate reports:

```bash
pytest --alluredir=reports
```

Open report:

```bash
allure serve reports
```

---

# CI/CD

The framework includes GitHub Actions integration for automated test execution on push.

---

# Example Logs

```text
[1ce5fa24] REQUEST -> POST https://reqres.in/api/users

[1ce5fa24] RESPONSE <- 201 POST https://reqres.in/api/users | 2393.55 ms
```

---

# Key Engineering Highlights

- Modular and scalable architecture
- Centralized API handling
- Reduced flaky test behavior through mocking
- Production-style logging strategy
- Environment-driven configuration
- Clean separation of concerns
- Reusable validation and assertion layers

---

# Future Improvements

- Pydantic response models
- Parallel execution using pytest-xdist
- Dockerized execution
- Performance testing integration
- Contract testing support

---