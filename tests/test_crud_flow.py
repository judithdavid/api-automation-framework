
from utils.validators import validate_status_code

def test_create_post(api_client):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = api_client.post("/posts", payload)

    validate_status_code(response, 201)

    data = response.json()

    assert data["title"] == "foo"
    assert data["body"] == "bar"