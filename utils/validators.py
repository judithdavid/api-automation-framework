from jsonschema import validate, ValidationError

def validate_json_key(response, key):
    body = response.json()
    assert key in body, (
        f"Expected key '{key}' in response. "
        f"Actual keys: {list(body.keys())}"
    )


def validate_json_schema(response, schema):
   
    validate_json_schema_data(response.json(), schema)

    
def validate_json_schema_data(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise AssertionError(
            f"Schema validation failed: {e.message}\n"
            f"Data: {data}"
        )
    
def validate_response_data_schema(response, schema):
    data = response.json().get("data")

    assert data is not None, "Response missing 'data' field"

    validate_json_schema_data(data, schema)