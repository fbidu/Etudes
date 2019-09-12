from random import randint
import pytest

@pytest.fixture
def client():
    return "potato"

@pytest.fixture
def user():

    def _user(name):
        data = {
            "name": name,
            "age": randint(20, 40)
        }

        return data

    return _user

def test_potato(client):
    assert client == "potato"

def test_client(user):
    u = user("João")

    assert isinstance(u, dict)
    assert u["name"] == "João"
    assert isinstance(u["age"], int)
    assert 20 <= u["age"] <= 40