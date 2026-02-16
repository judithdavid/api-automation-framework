def validate_status_code(response, expected):
    actual = response.status_code
    assert actual == expected, (
        f"Expected {expected}, got {actual}. "
        f"Response: {response.text}"
    )


def validate_json_key(response, key):
    body = response.json()
    assert key in body, (
        f"Expected key '{key}' in response. "
        f"Actual keys: {list(body.keys())}"
    )