# ============================================================
#  PYTEST — lo esencial
#  Ejecuta: python -m pytest 07_testing/learn/
# ============================================================


# Funciones a testear
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# Tests básicos
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError, match="dividir por cero"):
        divide(10, 0)


def test_palindrome():
    assert is_palindrome("oso")
    assert is_palindrome("Anita lava la tina")
    assert not is_palindrome("python")


# Parametrize — probar múltiples inputs
import pytest

@pytest.mark.parametrize("input,expected", [
    ("oso", True),
    ("python", False),
    ("Anita lava la tina", True),
    ("", True),
    ("a", True),
])
def test_palindrome_parametrized(input, expected):
    assert is_palindrome(input) == expected
