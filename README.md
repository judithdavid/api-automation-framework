
# API Automation Framework

## Overview

A modular API automation framework built with Python, PyTest, and Requests, featuring reusable client architecture, centralized validation, parametrized testing, and environment-driven configuration for REST API validation.

---

## Test API Used

This framework currently validates public REST APIs from:

https://jsonplaceholder.typicode.com

---

## Tech Stack

* Python 3.x
* PyTest
* Requests
* Virtual Environment (venv)
* Git / GitHub

---

## Framework Architecture

```
api-automation-framework/
│
├── config/
│   └── config.py
│
├── clients/
│   └── api_client.py
│
├── utils/
│   └── validators.py
│
├── tests/
│   ├── test_users.py
│   ├── test_crud_flow.py
│   └── test_negative.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Key Features

* Reusable API client using `requests.Session`
* Centralized environment configuration
* Parametrized test execution
* Smoke test tagging
* Positive and negative test coverage
* CRUD flow validation
* Centralized response validation utilities
* Clean separation of concerns

---

## Test Coverage

The framework currently validates:

* GET multiple users
* GET single user (parametrized)
* Create resource (POST)
* Negative endpoint validation (404 handling)

---

## How to Run the Project

### 1. Create Virtual Environment

```
python -m venv venv
```

### 2. Activate Environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Tests

Run all tests:

```
pytest
```

Run verbose:

```
pytest -v
```

Run only smoke tests:

```
pytest -m smoke
```

---

## Environment Configuration

The base URL can be overridden using an environment variable.

Windows:

```
set API_BASE_URL=https://your-api-url.com
pytest
```

Mac/Linux:

```
export API_BASE_URL=https://your-api-url.com
pytest
```

If not set, the framework defaults to:

```
https://jsonplaceholder.typicode.com
```

---


