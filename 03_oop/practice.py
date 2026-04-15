# ============================================================
#  PRÁCTICA — OOP
#  Escribe tu solución donde dice ... y ejecuta el archivo.
# ============================================================

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


# Ejercicio 1: Clase básica
# Crea una clase Counter con __init__(start=0), increment(), y value (property).

# class Counter: ...

ejercicio(1, "clase Counter",
    lambda: ...,  # c = Counter(5); c.increment(); c.increment(); c.value -> 7
    7,
)


# Ejercicio 2: __repr__ y __str__
# Crea una clase Point(x, y) con:
# repr: "Point(3, 4)"  str: "(3, 4)"

# class Point: ...

ejercicio(2, "__repr__ y __str__",
    lambda: ...,  # (repr(Point(3, 4)), str(Point(3, 4)))
    ("Point(3, 4)", "(3, 4)"),
)


# Ejercicio 3: __add__
# Haz que dos Point se puedan sumar: Point(1, 2) + Point(3, 4) == Point(4, 6)

ejercicio(3, "__add__ en Point",
    lambda: ...,  # repr(Point(1, 2) + Point(3, 4))
    "Point(4, 6)",
)


# Ejercicio 4: __eq__ y __lt__
# Dos Points son iguales si tienen mismo x e y.
# Un Point es menor si su distancia al origen es menor.
# Pista: distancia = (x**2 + y**2) ** 0.5

ejercicio(4, "__eq__ y __lt__",
    lambda: ...,  # (Point(1, 2) == Point(1, 2), Point(1, 1) < Point(3, 4))
    (True, True),
)


# Ejercicio 5: @property
# Crea Rectangle(width, height) con propiedad `area`.

# class Rectangle: ...

ejercicio(5, "property area",
    lambda: ...,  # Rectangle(5, 3).area
    15,
)


# Ejercicio 6: Herencia
# Crea Square(side) que herede de Rectangle.
# Square(5).area debe ser 25.

# class Square(Rectangle): ...

ejercicio(6, "herencia Square",
    lambda: ...,  # (Square(5).area, isinstance(Square(5), Rectangle))
    (25, True),
)


# Ejercicio 7: dataclass básico
# Crea un dataclass Product(name, price, quantity=1).
# from dataclasses import dataclass

ejercicio(7, "dataclass Product",
    lambda: ...,  # (Product("café", 3.5).name, Product("café", 3.5) == Product("café", 3.5))
    ("café", True),
)


# Ejercicio 8: dataclass con método
# Agrega un método total() a Product que retorne price * quantity.

ejercicio(8, "dataclass con método",
    lambda: ...,  # Product("café", 3.5, 4).total()
    14.0,
)


# Ejercicio 9: __contains__
# Crea Playlist(songs: list[str]) donde "in" busque canciones.
# "bohemian" in Playlist(["Bohemian Rhapsody", "Stairway"]) -> True (case-insensitive)

# class Playlist: ...

ejercicio(9, "__contains__ case-insensitive",
    lambda: ...,  # ("bohemian" in p, "hello" in p)
    (True, False),
)


# Ejercicio 10: __len__ y __getitem__
# Haz que Playlist soporte len() y acceso por índice playlist[0].

ejercicio(10, "__len__ y __getitem__",
    lambda: ...,  # (len(p), p[0])
    (3, "Bohemian Rhapsody"),
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
