import responses
from core.response import APIResponse


@responses.activate
def test_mock_users(api_client):
    responses.add(
        responses.GET,
        "https://reqres.in/api/users",
        json={"data": [{"id": 1, "email": "test@test.com"}]},
        status=200
    )

    resp = APIResponse(api_client.get("/users"))

    assert resp.status == 200
    assert resp.data[0]["id"] == 1