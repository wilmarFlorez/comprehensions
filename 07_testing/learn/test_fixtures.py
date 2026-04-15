# ============================================================
#  FIXTURES Y MOCKS
#  Ejecuta: python -m pytest 07_testing/learn/test_fixtures.py -v
# ============================================================
import pytest
from unittest.mock import Mock, patch


# Fixtures — setup reutilizable
@pytest.fixture
def users():
    return [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "viewer"},
        {"name": "Charlie", "role": "editor"},
    ]


@pytest.fixture
def admins(users):
    """Fixture que depende de otra fixture."""
    return [u for u in users if u["role"] == "admin"]


def test_users_count(users):
    assert len(users) == 3


def test_admins(admins):
    assert len(admins) == 1
    assert admins[0]["name"] == "Alice"


# Mock — simular dependencias externas
class UserService:
    def __init__(self, api_client):
        self.api = api_client

    def get_user_name(self, user_id):
        response = self.api.get(f"/users/{user_id}")
        return response["name"]


def test_get_user_name():
    # Crear un mock del API client
    mock_api = Mock()
    mock_api.get.return_value = {"name": "Alice", "id": 1}

    service = UserService(mock_api)
    name = service.get_user_name(1)

    assert name == "Alice"
    mock_api.get.assert_called_once_with("/users/1")


# Patch — reemplazar temporalmente un módulo/función
import time

def slow_function():
    time.sleep(5)
    return "done"

def test_slow_function_with_patch():
    with patch("time.sleep"):  # sleep no hace nada
        result = slow_function()
    assert result == "done"
