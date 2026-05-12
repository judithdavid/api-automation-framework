from core.response import APIResponse
from core.assertions import assert_status
import pytest

@pytest.mark.regression
def test_create_and_update_user(api_client):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    create_res = APIResponse(api_client.post("/users", payload))
    assert_status(create_res, 201)

    data = create_res.body

    assert data["name"] == "morpheus"
    assert "id" in data

    user_id = data["id"]

    update_payload = {
        "name": "neo",
        "job": "the one"
    }

    update_res = APIResponse(
    api_client.put(f"/users/{user_id}", update_payload)
)

    assert_status(update_res, 200)

    updated = update_res.body

    assert updated["name"] == "neo"

    
