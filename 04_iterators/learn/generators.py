# ============================================================
#  GENERATORS — yield, send(), custom iterators
# ============================================================


# Generator básico con yield
def countdown(n):
    """Cuenta regresiva desde n hasta 1."""
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num, end=" ")
print()  # 5 4 3 2 1


# Generator infinito
def fibonacci():
    """Genera la secuencia de Fibonacci infinitamente."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Tomar los primeros 10
from itertools import islice

print(list(islice(fibonacci(), 10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# yield from — delegar a otro generador
def flatten(nested):
    """Aplana una lista anidada de cualquier profundidad."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

data = [1, [2, 3], [4, [5, 6]], 7]
print(list(flatten(data)))  # [1, 2, 3, 4, 5, 6, 7]


# Protocolo de iterador: __iter__ y __next__
class FileLines:
    """Itera sobre líneas de un archivo simulado."""

    def __init__(self, lines):
        self._lines = lines
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._lines):
            raise StopIteration
        line = self._lines[self._index]
        self._index += 1
        return line.strip()


reader = FileLines(["  hola  ", "  mundo  ", "  python  "])
for line in reader:
    print(f"-> {line}")
