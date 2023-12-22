import pytest
from chekpost import get_login

@pytest.fixture()
def token():
    return get_login()