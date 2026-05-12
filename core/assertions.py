def assert_status(resp, expected):
    assert resp.status == expected, (
        f"[STATUS FAIL] Expected {expected}, got {resp.status}\n"
        f"Response: {resp.body}"
    )


def assert_list(data):
    assert isinstance(data, list), (
        f"[TYPE FAIL] Expected list, got {type(data)}"
    )


def assert_not_empty(data):
    assert data, "[EMPTY FAIL] Response data is empty"


def assert_key(obj, key):
    assert key in obj, f"[KEY FAIL] Missing key '{key}' in {obj}"