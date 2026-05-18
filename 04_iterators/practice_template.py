# ============================================================
#  PRÁCTICA — ITERADORES Y GENERATORS
#  Escribe tu solución donde dice ... y ejecuta el archivo.
# ============================================================
from itertools import islice

passed = 0
total = 10


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


# Ejercicio 1: Generator básico
# Crea un generator `evens(n)` que yield los primeros n números pares (0, 2, 4, ...).

def evens(n):
    ...  # tu solución aquí

ejercicio(1, "generator evens",
    lambda: list(evens(5)),
    [0, 2, 4, 6, 8],
)


# Ejercicio 2: Generator expression
# Suma los cuadrados de 1 a 100 usando un generator expression (NO list comp).

ejercicio(2, "sum con generator",
    lambda: ...,  # sum(... generator expression ...)
    338350,
)


# Ejercicio 3: yield from
# Crea flatten(nested) que aplane una lista anidada un solo nivel.
# flatten([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]

def flatten(nested):
    ...  # usa yield from

ejercicio(3, "yield from flatten",
    lambda: list(flatten([[1, 2], [3, 4], [5]])),
    [1, 2, 3, 4, 5],
)


# Ejercicio 4: itertools.chain
# Concatena tres listas sin crear una nueva lista intermedia.

a = [1, 2, 3]
b = [4, 5]
c = [6, 7, 8, 9]

ejercicio(4, "itertools.chain",
    lambda: ...,  # usa itertools.chain
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
)


# Ejercicio 5: islice con generator infinito
# Crea un generator `powers_of_2()` infinito (1, 2, 4, 8, 16, ...)
# Toma los primeros 8 con islice.

def powers_of_2():
    ...  # tu solución aquí

ejercicio(5, "islice + generator infinito",
    lambda: list(islice(powers_of_2(), 8)),
    [1, 2, 4, 8, 16, 32, 64, 128],
)


# Ejercicio 6: itertools.groupby
# Agrupa palabras por su primera letra. Input ya está ordenado.
words = ["apple", "avocado", "banana", "blueberry", "cherry", "coconut"]

ejercicio(6, "groupby primera letra",
    lambda: ...,  # dict con {letra: [palabras]}
    {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry", "coconut"]},
)


# Ejercicio 7: Protocolo de iterador
# Crea una clase Repeat(value, times) que sea iterable.
# list(Repeat("hola", 3)) -> ["hola", "hola", "hola"]

# class Repeat: ...  # implementa __iter__ y __next__

ejercicio(7, "protocolo iterador",
    lambda: ...,  # list(Repeat("hola", 3))
    ["hola", "hola", "hola"],
)


# Ejercicio 8: itertools.product
# Genera todas las combinaciones de ["A", "B"] y [1, 2, 3].

ejercicio(8, "itertools.product",
    lambda: ...,
    [("A", 1), ("A", 2), ("A", 3), ("B", 1), ("B", 2), ("B", 3)],
)


# Ejercicio 9: Generator como pipeline
# Crea un pipeline de generators:
# 1. nums(): yield 1..10
# 2. doubled(gen): yield cada elemento * 2
# 3. only_big(gen): yield solo los >= 10

ejercicio(9, "pipeline de generators",
    lambda: ...,  # list(only_big(doubled(nums())))
    [10, 12, 14, 16, 18, 20],
)


# Ejercicio 10: zip_longest
# Combina dos listas de distinta longitud, rellenando con "-".

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87]

ejercicio(10, "zip_longest",
    lambda: ...,  # list(zip_longest(...))
    [("Alice", 95), ("Bob", 87), ("Charlie", "-")],
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
