import pytest
from app import app


def test_assert():
    assert True


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_create_post_page(client):
    response = client.get('/pages/create_post.html')
    assert response.status_code == 200


@pytest.fixture
def client():
    client = app.test_client()
    return client
