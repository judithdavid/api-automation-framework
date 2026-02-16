
import pytest
from utils.validators import validate_status_code


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_multiple_users(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    validate_status_code(response, 200)

@pytest.mark.smoke
def test_get_users(api_client):
    response = api_client.get("/users")

    validate_status_code(response, 200)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]