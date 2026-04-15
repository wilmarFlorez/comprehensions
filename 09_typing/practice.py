# ============================================================
#  PRÁCTICA — TYPING
#  Agrega los type hints correctos a cada función.
#  Ejecuta: python -m mypy 09_typing/practice.py
# ============================================================

passed = 0
total = 8


def ejercicio(num, descripcion, solucion, esperado):
    global passed
    try:
        resultado = solucion()
        if resultado is ...:
            print(f"- Ejercicio {num}: {descripcion} — pendiente")
            return
        assert resultado == esperado, f"{resultado}"
        passed += 1
        print(f"✓ Ejercicio {num}: {descripcion} — OK")
    except AssertionError as e:
        print(f"✗ Ejercicio {num}: {descripcion} — FALLÓ: {e}")
    except Exception:
        print(f"- Ejercicio {num}: {descripcion} — pendiente")


# Ejercicio 1: Tipos básicos
# Agrega type hints a la función: parámetros y retorno.

def repeat(text, times):  # -> añade hints: (text: str, times: int) -> str
    return text * times

ejercicio(1, "type hints básicos",
    lambda: repeat("ha", 3),
    "hahaha",
)


# Ejercicio 2: Contenedores
# Agrega types a esta función que filtra números pares.

def filter_evens(numbers):  # -> (numbers: list[int]) -> list[int]
    return [n for n in numbers if n % 2 == 0]

ejercicio(2, "type hints contenedores",
    lambda: filter_evens([1, 2, 3, 4, 5, 6]),
    [2, 4, 6],
)


# Ejercicio 3: Optional
# Crea safe_get(d, key) que retorne el valor o None.
# Type hints: (d: dict[str, int], key: str) -> int | None

def safe_get(d, key):
    ...  # tu solución aquí

ejercicio(3, "Optional return",
    lambda: (safe_get({"a": 1, "b": 2}, "a"), safe_get({"a": 1}, "c")),
    (1, None),
)


# Ejercicio 4: Callable como parámetro
# Agrega type hints: transform recibe un Callable[[str], str] y una lista de strings.
from typing import Callable

def transform_all(func, items):  # hints: Callable[[str], str], list[str]) -> list[str]
    return [func(item) for item in items]

ejercicio(4, "Callable type",
    lambda: transform_all(str.upper, ["hola", "mundo"]),
    ["HOLA", "MUNDO"],
)


# Ejercicio 5: TypeVar genérico
# Crea last(items) que retorne el último elemento de cualquier lista.
# Debe funcionar con list[int], list[str], etc.
from typing import TypeVar

T = TypeVar("T")

def last(items):  # -> (items: list[T]) -> T
    ...  # tu solución aquí

ejercicio(5, "TypeVar genérico",
    lambda: (last([1, 2, 3]), last(["a", "b", "c"])),
    (3, "c"),
)


# Ejercicio 6: Protocol
# Crea un Protocol `HasName` con atributo `name: str`.
# Crea una función get_names(items: list[HasName]) -> list[str].
from typing import Protocol

# class HasName(Protocol): ...
# def get_names(items): ...

ejercicio(6, "Protocol",
    lambda: ...,
    ["Alice", "Bob"],
)


# Ejercicio 7: Union / |
# Crea stringify(value) que acepte int | float | str y retorne str.

def stringify(value):  # -> (value: int | float | str) -> str
    ...  # tu solución aquí

ejercicio(7, "Union types",
    lambda: (stringify(42), stringify(3.14), stringify("hi")),
    ("42", "3.14", "hi"),
)


# Ejercicio 8: TypedDict
# Crea un TypedDict para un User con name: str y age: int.
from typing import TypedDict

# class User(TypedDict): ...

def create_user(name, age):  # -> User
    ...  # tu solución aquí

ejercicio(8, "TypedDict",
    lambda: ...,  # create_user("Alice", 30)
    {"name": "Alice", "age": 30},
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
