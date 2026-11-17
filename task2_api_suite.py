import pytest
import requests
from pydantic import BaseModel

BASE_URL = "https://jsonplaceholder.typicode.com"


# Pydantic Schema Definition
class PostSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str


# Response time < 2 seconds
def test_response_time():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert response.status_code == 200
    assert (
        response.elapsed.total_seconds() < 2.0
    ), f"Response time took longer than 2s: {response.elapsed.total_seconds()}s"


# Schema validation (use pydantic or jsonschema)
def test_schema_validation():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert response.status_code == 200

    # Validate using Pydantic (raises ValidationError if invalid)
    post_data = PostSchema(**response.json())
    assert post_data.id == 1


# Parameterized test: Validate multiple endpoints (e.g., /posts, /comments, /users)
@pytest.mark.parametrize(
    "endpoint, expected_status",
    [("/posts", 200), ("/comments", 200), ("/users", 200)],
)
def test_multiple_endpoints(endpoint, expected_status):
    response = requests.get(f"{BASE_URL}{endpoint}", timeout=10)
    assert response.status_code == expected_status
    assert len(response.json()) > 0