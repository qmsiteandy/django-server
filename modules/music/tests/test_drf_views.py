import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_post_music():
    data = {
        "song": "Song123",
        "singer": "Singer123"
    }
    client = APIClient()
    response = client.post(path="/api/music/", data=data, format="json")
    assert response.status_code == 201
    response = client.get(path="/api/music/")
    assert len(response.json()) == 1
