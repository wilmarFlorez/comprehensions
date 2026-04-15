# ============================================================
#  TYPE HINTS — lo esencial para código profesional
# ============================================================
from typing import Optional


# Básico: funciones
def greet(name: str, times: int = 1) -> str:
    return (f"Hola, {name}! " * times).strip()


# Contenedores
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def word_count(text: str) -> dict[str, int]:
    words = text.lower().split()
    result: dict[str, int] = {}
    for w in words:
        result[w] = result.get(w, 0) + 1
    return result


# Optional — puede ser None
def find_user(user_id: int) -> Optional[dict]:
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)


# Union (Python 3.10+ puede usar |)
def process(value: int | str) -> str:
    if isinstance(value, int):
        return f"número: {value}"
    return f"texto: {value}"


# TypeAlias
type UserID = int
type UserMap = dict[UserID, str]

users: UserMap = {1: "Alice", 2: "Bob"}


# Callable
from typing import Callable


def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

result = apply_twice(lambda x: x * 2, 3)  # 12
print(f"apply_twice: {result}")


# TypeVar y Generic
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T | None:
    return items[0] if items else None

print(f"first([1,2,3]): {first([1, 2, 3])}")
print(f"first(['a','b']): {first(['a', 'b'])}")
