
from core.response import APIResponse
from core.assertions import assert_status, assert_list, assert_not_empty, assert_key
from schemas.user_schema import USER_SCHEMA
from utils.validators import validate_json_schema_data
import pytest

@pytest.mark.smoke
def test_get_users(api_client):
    resp = APIResponse(api_client.get("/users"))

    # Layer 1: Transport
    assert_status(resp, 200)

    # Layer 2: Structure
    users = resp.data
    assert_list(users)
    assert_not_empty(users)

    # Layer 3: Contract
    for user in users:
        validate_json_schema_data(user, USER_SCHEMA)

    # Layer 4: Business sanity
    assert_key(users[0], "id")