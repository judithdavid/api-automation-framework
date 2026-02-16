from utils.validators import validate_status_code

def test_invalid_endpoint(api_client):
    response = api_client.get("/invalidendpoint")

    validate_status_code(response, 404)