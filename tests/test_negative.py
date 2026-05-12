
from core.response import APIResponse
from core.assertions import assert_status


def test_invalid_endpoint(api_client):
    resp = APIResponse(api_client.get("/invalidendpoint"))

    assert_status(resp, 200)
