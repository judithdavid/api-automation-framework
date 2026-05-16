import pytest
from core.response import APIResponse
from core.assertions import assert_status


@pytest.mark.regression
def test_delete_user(api_client):

    response = APIResponse(
        api_client.delete("/users/2")
    )

    assert_status(response, 204)