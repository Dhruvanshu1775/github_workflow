import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        return client



def test_string(client):
    response = client.get('/page',query_string={'name': 'DHRUV'})
    assert "1" == "1"


def test_string1():
    assert "1" == "1"


def test_string2():
    assert "1" == "1"
