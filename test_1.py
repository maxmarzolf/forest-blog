import pytest
from app import forest_blog


def test_assert():
    assert True


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.fixture
def client():
    client = forest_blog.test_client()
    return client
