# tests/test_crud_flow.py
# def test_create_user(api_client):
#     payload = {
#         "name": "morpheus",
#         "job": "leader"
#     }

#     response = api_client.post("/users", payload)

#     assert response.status_code == 201
#     data = response.json()

#     assert data["name"] == "morpheus"
#     assert data["job"] == "leader"


#working

# def test_create_post(api_client):
#     payload = {
#         "title": "foo",
#         "body": "bar",
#         "userId": 1
#     }

#     response = api_client.post("/posts", payload)

#     assert response.status_code == 201

#     data = response.json()

#     assert data["title"] == "foo"
#     assert data["body"] == "bar"
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