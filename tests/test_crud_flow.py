
def test_create_user(api_client):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "morpheus"
    assert data["job"] == "leader"


